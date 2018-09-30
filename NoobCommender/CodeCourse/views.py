from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.db.models import Count,Sum,Q
from django.http import HttpResponseRedirect
from django.db.models.functions import Coalesce
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView,View
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .CustomCourses import(
    create_custom_course,
    append_problems_course
)
from CoreEngine.models import SolvedProblems
from CodeChefAPI_Oauth2.GetUserDetails import async_model_task
from CodeChefAPI_Oauth2.service import CodeChefAPIUtitlity
from .models import (
    Problem,
    Course,
    TakenCourse
)

# Create your views here.

class CourseListView(ListView):
    model = Course
    ordering = ('name', )
    context_object_name = 'courses'
    template_name = 'course/course_list.html'

    def get_queryset(self): 
        programmer = self.request.user.programmer
        taken_courses = programmer.courses.values_list('owner', flat=True)
        queryset = Course.objects.all() \
            .exclude(owner__in=taken_courses) \
            .annotate(problems_count=Count('problems')) \
            .annotate(collective_points = Sum('problems__problem_points'))\
            .annotate(solved_problem_points = Coalesce(
                    Sum('problems__problem_points',\
                    filter=Q(problems__is_solved = True)),0\
            ))\
            .filter(problems_count__gt=0)
            
        return queryset

class TakenCourseListView(ListView):
    model = TakenCourse
    context_object_name = 'opt_courses'
    template_name = 'course/taken_course_list.html'

    def get_queryset(self):
        queryset = self.request.user.programmer.opt_courses \
            .select_related('course') \
            .order_by('course__name')
        return queryset

@transaction.atomic
@login_required
def create_new_course(request):
    user = request.user
    util = CodeChefAPIUtitlity(access_token = user.access_token,\
            refresh_token = user.refresh_token)

    if user.create_default_course:
        
        # if no prior course exists .... check for prior experience
        # if no prior experience exists .... go for default course...
        
        #Create two default courses ...

        dfc = util.get_questions_([],default=True)
        dfc = [x for x in dfc]
        dfc = [dfc[:len(dfc)//2],dfc[len(dfc)//2:]]
            
        for i in range(2):
            course_name = "Default Course {}".format(i+1)
            append_problems_course(request,course_name,dfc[i],tag="BEG-EASY")
        
        user.create_default_course = False
        user.save()
        messages.success(request,"Default Course created due to lack of experience !")
    if not user.create_custom_course and user.band:
        create_custom_course(request)
    else:
        messages.info(request,"User Have Zero Band")
        
    return redirect('dashboard')



@login_required
def take_course(request,pk):
    course = get_object_or_404(Course,pk=pk)

    problem_set = Problem.objects.filter(course=course.id)
    return render(request,'course/solve_problem.html',{
        'problem_set':problem_set,
    })

@transaction.atomic
@login_required
def add_to_TODO(request,id,problem_code):
    user  = request.user
    util = CodeChefAPIUtitlity(
        access_token=user.access_token,
        refresh_token = user.refresh_token
    )
    problem = Problem.objects.get(
        user = user,
        problem_code = problem_code
    )
    problem.problem_TODO = True
    problem.save()
    try:
        msg = util.add_TODO(problem_code)
        messages.success(request,"Problem Added to TODO")
    except:
        print(msg)
        messages.error(request,"Server Error Occured ... ")

    #After every new problem is Added to TODO 
    #spawn a async task for updating user tokens
    #and updating solved problems
    async_model_task.delay(request.user.id)
    return redirect('dashboard')
