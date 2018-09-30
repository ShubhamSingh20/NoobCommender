from CoreEngine.models import SolvedProblems
from CodeCourse.models import Course,Problem
from .service import FetchAPIresponse
from django.contrib.auth import get_user_model

from celery.task.schedules import crontab
from celery.decorators import task
from celery.utils.log import get_task_logger
import celery

logger = get_task_logger(__name__)

User = get_user_model()

URL_ME = "https://api.codechef.com/users/me"

class UpdateDjangoObjects(object):
    @classmethod
    def update_user_attribute(cls,current_user,**kwargs):
        if 'first_name' in kwargs and 'last_name' in kwargs:
            current_user.first_name = kwargs.get('first_name')
            current_user.last_name = kwargs.get('last_name')
            current_user.create_default_course = kwargs.get('create_default_course')

        #If the band of the user progresses... Re initalize 
        #the q_index(index for the cluster storage) to 0
        band = str(kwargs.get('band'))

        if current_user.band != band:
                current_user.q_index = 1
                current_user.band = band 

        current_user.refresh_token = kwargs.get('refresh_token')
        current_user.access_token = kwargs.get('access_token')
        current_user.save()
        
        return current_user

    @classmethod
    def save_user_contest_details(cls,cur_user_,**kwargs):
        solved_problems = kwargs.get('solved_problems')
        final_solved_set = solved_problems

        created_cur_user = SolvedProblems.objects.filter(
            user = cur_user_
        ).exists()

        if created_cur_user:
            db_solved_problems = SolvedProblems.objects.filter(
                user = cur_user_
            ).values_list('solved_cc',flat=True)
        
            db_solved_problems = set(list(db_solved_problems))
            solved_problems = set(solved_problems)
            final_solved_set = solved_problems.difference(db_solved_problems)
            final_solved_set = list(final_solved_set)

        for i in final_solved_set:
            cur_solved_problem = SolvedProblems.objects.create(
                user = cur_user_,
                solved_cc = i,
        )
            cur_solved_problem.save()

            
        cur_user_.save()
        return cur_user_

class GetUserDetiails:
    def __init__(self,**kwargs):
        self.access_token = kwargs.get('access_token')
    
    def update_details(self):
        
        FetchAPI = FetchAPIresponse(access_token = self.access_token)
        current_user_details = FetchAPI.make_requests(URL_ME)

        band = current_user_details['band'].replace('★','')
        
        try:
            band = int(band.encode('ascii','ignore'))
        except:
            band = 0
        
        # If user never solved a problem create a default course..
        # for that user consisting of top 20 easy level questions
        create_default_course = not bool(band)
        current_user_username = current_user_details['username']
        contest_details = current_user_details[ "problemStats"]
        _first_name,_last_name = current_user_details['fullname'].split(' ')

        try:
            solved_problems = contest_details['solved']['Practice Problems']
        except:
            solved_problems = []
        print(solved_problems)
        return {
            'current_user_username':current_user_username,
            'first_name':_first_name,
            'last_name' : _last_name,
            'solved_problems':solved_problems,
            'band':band,
            'create_default_course':create_default_course
        }
        

class AsncyTask(object):
    def __init__(self,**kwargs):
        if "id" in kwargs:
            self.user = User.objects.get(id = kwargs.get("id"))
            self.get_user_details = GetUserDetiails(access_token = self.user.access_token)
        else:
            self.user = kwargs.get("user")

    def update_tokens(self):
        util = FetchAPIresponse(refresh_token = self.user.refresh_token)
        tokens_ = util.get_new_access_from_refresh_token()
        update = UpdateDjangoObjects()
        logger.info(tokens_)
        update.update_user_attribute(
            self.user,
            band = self.user.band,
            access_token = tokens_['access_token'],
            refresh_token = tokens_['refresh_token']
        )

    
    def update_solved_points(self):
        user_courses = Course.objects.filter(
            owner = self.user
        )        

        if not user_courses:
            #If no courses for the current user...
            return 
        
        solved_problems = self.get_user_details.update_details()['solved_problems']
        
        for courses_ in user_courses:
            #get all the problems of a particular course
            current_course_problems = Problem.objects.filter(
                course = courses_
            ) 
            current_course_problems_list = current_course_problems.values_list('problem_code',flat=True)
            print(current_course_problems_list)
            for solved in solved_problems:
                if solved in current_course_problems_list:
                    get_problem = Problem.objects.get(
                        problem_code = solved
                    )
                    print(get_problem.problem_code)
                    get_problem.is_solved = True
                    get_problem.save()
    
@celery.task(name='async.model.token.update')
def async_model_task(id):   
    task = AsncyTask(id=id)
    task.update_tokens()


@celery.task(name='async.model.user.score.update')
def async_score_task(id):   
    task = AsncyTask(id = id)
    task.update_solved_points()