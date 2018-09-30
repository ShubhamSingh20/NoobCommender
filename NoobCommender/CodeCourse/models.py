from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

# Create your models here.
class User(AbstractUser):
    access_token = models.CharField(max_length = 50)
    refresh_token = models.CharField(max_length = 50)
    band = models.CharField(max_length=5)
    create_default_course = models.BooleanField(default=False)
    lock = models.BooleanField(default=False)
    q_index = models.PositiveSmallIntegerField(default=1)
    slug = models.UUIDField(
        default=uuid.uuid4,
        blank=True,
        editable=False
    )

class Course(models.Model):
    name = models.CharField(max_length = 50)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    tag = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Problem(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='problems')
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null = True)
    problem_code = models.CharField(max_length=10,default = "apple 1")
    contest_code = models.CharField(max_length=10,default = "apple 1")
    problem_TODO = models.BooleanField(default=False)
    is_solved = models.BooleanField(default=False)
    problem_points = models.FloatField(default=10.0)

    def __str__(self):
        return self.problem_code

class Programmer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    courses = models.ManyToManyField(Course,through='TakenCourse')

    
    def get_problems(self,course,**kwargs):

        solved_problems = self.problem_solutions.filter(\
            solution__problem__course=course).\
            values_list('solution__problem__pk',flat = True
        )

        if "solved_problems" in kwargs:
            return solved_problems
        problems = course.problems.exclude(pk__in=solved_problems).order_by('problem_code')
        
        if "unsolved_problems" in kwargs:
            return problems
        

    def __str__(self):
        return self.user.username

class TakenCourse(models.Model):
    user = models.ForeignKey(Programmer,on_delete=models.CASCADE,related_name='opt_courses')
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='opt_courses')
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
