from django.db import models
from authentication_app.models import JobSeeker, JobProvider

# Create your models here.

class Appointment(models.Model):
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, related_name='appointments')
    job_provider = models.ForeignKey(JobProvider, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed')
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-appointment_date', '-start_time']

    def __str__(self):
        return f"{self.job_provider.company_name} -> {self.job_seeker.first_name} on {self.appointment_date}"
