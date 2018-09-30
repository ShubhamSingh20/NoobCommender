from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login,authenticate,get_user_model,forms
from django.views.generic import CreateView,TemplateView
from braces.views import AnonymousRequiredMixin
from authtools import views as authenticationViews
from django.db import transaction
from django.contrib import messages


from CodeCourse.models import Programmer
from .GetUserDetails import (
    GetUserDetiails,
    UpdateDjangoObjects,
    async_score_task
)
from .service import FetchAPIresponse
from .forms import SignUpForm


# Create your views here.
User = get_user_model()
AUTH_TOKEN = None


# Response fro GetUserDetails
# 'current_user_username':current_user_username,
# 'first_name':_first_name,
# 'last_name' : _last_name,
# 'solved_problems':solved_problems,
# 'band':band,
# 'create_default_course':create_default_course
#     

class HomeSignUp(TemplateView):
    template_name = 'registration/HomeSignup.html'

class LogInView(authenticationViews.LoginView,AnonymousRequiredMixin):

    form_class = forms.AuthenticationForm
    template_name = 'registration/login.html'

    @transaction.atomic
    def dispatch(self, *args, **kwargs):
        return super(LogInView, self).dispatch(*args, **kwargs)

    def form_valid(self,form):
        _username = form.cleaned_data['username']
        _password = form.cleaned_data['password']

        _user = authenticate(username=_username,password=_password)

        if _user is not None:
            current_refresh_token = _user.refresh_token
            FetchAPI = FetchAPIresponse(refresh_token=current_refresh_token)
            _tokens = FetchAPI.get_new_access_from_refresh_token()
            
            get_user_details = GetUserDetiails(access_token = _tokens['access_token'])
            user_details = get_user_details.update_details()
            
            _user = UpdateDjangoObjects.\
            update_user_attribute(
                _user,
                access_token = _tokens['access_token'],
                refresh_token = _tokens['refresh_token'],
                band = user_details['band'],
                create_default_course = user_details['create_default_course'],
            )
            
            _user = UpdateDjangoObjects.\
            save_user_contest_details(
                _user,
                solved_problems = user_details['solved_problems'],
            )
            async_score_task.delay(_user.id)
            login(self.request,_user)
            messages.success(self.request,"Successfully Logged In !")
            return redirect('dashboard')
        else:
            self.form_invalid(form)


class SignUpView(CreateView,AnonymousRequiredMixin):
    model = User
    form_class = SignUpForm
    template_name = 'registration/SignUp.html'

    
    @transaction.atomic
    def dispatch(self, *args, **kwargs):
        return super(SignUpView, self).dispatch(*args, **kwargs)

    def form_valid(self,form,*args,**kwargs):
        try:
            _user = User.objects.get(slug = self.kwargs.get("slug"))
        except ObjectDoesNotExist:
            #User does not exists
            self.form_invalid(form)
        
        current_password = form.cleaned_data['password1']
        _user.set_password(current_password)
        _user.save()
        try:
            authenticate(username=_user.username,password=current_password)
        except ObjectDoesNotExist:
            self.form_invalid(form)
        
        login(self.request,_user)
        messages.success(self.request,"Successfully Signed Up !!")
        return redirect('dashboard')


@transaction.atomic
def oauth_view(request):
    AUTH_TOKEN = request.GET.get('code',None)
        #Check for the redirect based flow.
        #if it's None then POST the url using Response

        #And then use this, to Fetch current_user_detail,
        #which includes access_token and refresh_token

    if request.user.is_anonymous and AUTH_TOKEN is None:
        return FetchAPIresponse().get_authentication_code()
    
    if AUTH_TOKEN is not None and not request.user.is_active:
        FetchAPI = FetchAPIresponse(auth_token=AUTH_TOKEN)
        access_token = FetchAPI.get_access_token()

        refresh_token = access_token['refresh_token']
        access_token = access_token['access_token']

        get_user_details = GetUserDetiails(access_token=access_token)
        user_details = get_user_details.update_details()
        
        #Username is under unique constraint 
        # if:
        #   username exists,
        #update the new access_token and refresh_token values.

        #Else: 
        #create a new user and assign all the values from the user
        #response.

        current_user,created = User.objects.get_or_create(
            username = user_details['current_user_username'],
        )
           
        if created:
            if user_details['solved_problems']:
                current_user = UpdateDjangoObjects.save_user_contest_details(
                    current_user,
                    solved_problems = user_details['solved_problems'],
            )

            current_user = UpdateDjangoObjects.\
            update_user_attribute(
                current_user,
                first_name = user_details['first_name'],
                last_name = user_details['last_name'],
                access_token = access_token,
                refresh_token = refresh_token,
                band = user_details['band'],
                create_default_course = user_details['create_default_course'],
            )
            Programmer.objects.create(user=current_user)
        else:
            
            current_user = UpdateDjangoObjects.\
            update_user_attribute(
                current_user,
                band = user_details['band'],
                access_token = access_token,
                refresh_token = refresh_token,
            )
            
            messages.info(request,"User already exists !")
            return redirect('login')
       
    return redirect('signup',slug=current_user.slug)

