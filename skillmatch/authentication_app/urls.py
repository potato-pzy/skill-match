from django.urls import path
from .views import *
urlpatterns = [
    path('signup/',signUp,name='signup'),
    path('login/',signIn,name='login'),
    path('',home,name='home'),
    path('logout/',logout_view,name='logout'),
    path('about/',about,name='about'),
]