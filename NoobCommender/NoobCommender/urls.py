"""NoobCommender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path


from CodeChefAPI_Oauth2.views import HomeSignUp,SignUpView,oauth_view,LogInView
from django.contrib.auth import views as auth_views

from CodeCourse.views import (
    create_new_course,
    take_course,
    CourseListView,
    TakenCourseListView,
    add_to_TODO,
)

urlpatterns = [
    path('',HomeSignUp.as_view(),name='HomeSignup'),
    path('signup/<slug:slug>',SignUpView.as_view(),name='signup'),
    path('oauth/',oauth_view,name='oauth'),
    path('dashboard/',CourseListView.as_view(),name='dashboard'),
    path('create/',create_new_course,name='create'),
    path('take/<int:pk>/',take_course,name='take_course'),
    path('add/<int:id>/<str:problem_code>/',add_to_TODO,name='add_TODO'),
    path('taken/',TakenCourseListView.as_view(), name='taken_course_list'),
    path('login/',LogInView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]
