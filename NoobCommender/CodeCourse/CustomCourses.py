from django.contrib import messages
from CoreEngine.prediction import fetch_tags
from CoreEngine.models import SolvedProblems
from CodeChefAPI_Oauth2.GetUserDetails import AsncyTask
from CodeChefAPI_Oauth2.service import CodeChefAPIUtitlity
from .models import (
    Problem,
    Course,
    TakenCourse
)

DEFAULT_CONTEST_CODE = "PRACTICE"

def append_problems_course(request,course_name,problem_list,tag):
    current_course = Course.objects.create(
        owner = request.user,
        name = course_name,
        tag = tag
    )
    current_course.save()

    for i in problem_list:
        current_prob = Problem.objects.create(
            course = current_course,
            problem_code = i,
            contest_code = DEFAULT_CONTEST_CODE
        )
        current_prob.save()

def create_custom_course(request):
    #check if there are any pending courses:
    #pending courses are  named as Pending_{serial_number}
    user  = request.user
    new_course = None
    
    try:
        new_course = Course.objects.filter(
            name__regex = r"^\PendingRecommendation+",
            owner = user,
        )[:1].get()
        
        new_course.name = "Recommendation {}".format(new_course.id)
        new_course.save()
        messages.success(request,"This recommendation is from PendingList...")
        return new_course
    except:
        
        #create a new course first get the predicted tags for the user...

        #check if tags exists or not
        #if not then fetch_tags() will return -1
        #in that case display -1 and return

        try:
            tag_list,course_id = fetch_tags(request)
        except:
            messages.error(request,"No more tags for current band...")
            return
        
        util = CodeChefAPIUtitlity(
            access_token = user.access_token,
            refresh_token = user.refresh_token,
        )

        problem_code_list = util.get_questions_(tag_list,default=False)

        if not problem_code_list:
            create_custom_course(request)

        try:
            problem_code_list = [x for x in problem_code_list]
        except:
            messages.error(request,"Some Error occurred.. Please try again !")
            return 

        # Get the problems which are not solved yet...
        #Since, problem_code_list may contain codes of 
        #already solved problems ... 

        db_solved_problems = SolvedProblems.objects.filter(
                user = user
            ).values_list('solved_cc',flat=True)

        db_solved_problems = set(list(db_solved_problems))
        problem_code_list = set(problem_code_list)

        final_solved_set = problem_code_list.difference(db_solved_problems)
        
        problem_code_list = list(final_solved_set)

        n_prob = len(problem_code_list)

        # if number of problems < 10 create a recommendation
        #else create recommendation and store the remaining
        #problem_code as PendingCourse
        if not n_prob:
            messages.info(request,"No new Questions Currently available try again later...")
            return
        if n_prob<10:
            append_problems_course(request,\
                "Recommendation {}".format(course_id),
                problem_code_list,
                ','.join(tag_list),
            )
        else:
            append_problems_course(request,\
                "Recommendation {}".format(course_id),
                problem_code_list[0:n_prob//2],
                ','.join(tag_list),
            )
            
            append_problems_course(request,\
                "PendingRecommendation {}".format(course_id),
                problem_code_list[n_prob//2:],
                ','.join(tag_list),
            )