from django.shortcuts import render
from myapp.models import *

# Create your views here.

def home(request):
    jobdata = Job.objects.all()

    data={
        "jobdata":jobdata
    }
    return render(request,'myapp/index.html',data)

def details(request, job_id):

    getData = Job.objects.get(id=job_id)

    getJOBData = {
        "getData":getData
    }
    return render(request,'myapp/details.html',getJOBData)