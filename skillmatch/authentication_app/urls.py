from django.urls import path
from .views import *
urlpatterns = [
    path('signup/',signUp),
    path('login/',signIn,name='login'),
    path('',home),
]