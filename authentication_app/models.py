from django.db import models
from django.contrib.auth.models import AbstractUser

job_roles = [
    ('electrician', 'electrician'),
    ('acservice', 'acservice'),
    ('plumber', 'plumber'),
    ('beautician','beautician'),
    ('dogwalker','dogwalker'),
    ('driver','driver'),
    ('homedeepcleaning','homedeepcleaning'),
    ('lawncare','lawncare'),
    ('lumberjack','lumberjack'),
    ('plantkeeper','plantkeeper'),
    ('welder','welder'),
    ('welldigger','welldigger'),
]

# Custom User model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_block = models.BooleanField(default=False)
    is_job_seeker = models.BooleanField(default=False)
    is_job_provider = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

# Model for storing JobSeeker information
class JobSeeker(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='job_seeker_profile')
    first_name = models.CharField(max_length=255)
    job_role = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    availability = models.JSONField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    area = models.CharField(max_length=255)
    profile = models.ImageField(upload_to='profiles/')

    def __str__(self):
        return self.first_name

# Model for storing JobProvider information
class JobProvider(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='job_provider_profile')
    company_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    profile = models.ImageField(upload_to='provider_profiles/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name




