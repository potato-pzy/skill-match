from django.shortcuts import render

# Create your views here.
def electrician_view(request):
    return render(request, 'indexcontent/electrician.html')