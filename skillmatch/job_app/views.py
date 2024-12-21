from django.shortcuts import render
from authentication_app.models import CustomUser,JobSeeker 
# Create your views here.
def electrician_view(request):
    electrician = JobSeeker.objects.select_related('user').filter(user__is_job_seeker=True)
    context = {
        'electrician':electrician,
    }
    return render(request, 'indexcontent/electrician.html',context)