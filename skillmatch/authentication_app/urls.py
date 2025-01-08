from django.urls import path
from .views import *
urlpatterns = [
    path('signup/',signUp,name='signup'),
    path('signup_job_seeker/',signUpJobSeeker,name='sign_up_job_seeker'),
    path('login/',signIn,name='login'),
    path('login_jobseaker/',signIn2,name='login_jobseaker'),
    path('',home,name='home'),
    path('logout/',logout_view,name='logout'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('who_are_you/',who_are_you,name='who_are_you'),

]