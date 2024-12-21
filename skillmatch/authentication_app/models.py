from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_block = models.BooleanField(default=False)
    is_job_seeker = models.BooleanField(default=False)
    
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
class JobSeeker(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=None)
    job_role = models.CharField(max_length=100)
    phone = models.CharField(max_length=100,null=True,blank=True,default=None)
    availability = models.CharField(max_length=100,null=True,blank=True,default=None)
    area = models.CharField(max_length=100,null=True,blank=True,default=None)
    profile = models.ImageField(upload_to='profile/',null=True,blank=True,default=None)