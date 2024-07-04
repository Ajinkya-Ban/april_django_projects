from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_view(request):
    return HttpResponse('<h1 style="color:red;">Hello Django...!</h1>')


def good_afternoon(request):
    return HttpResponse(
        '<h1 style="color:purple; text-decoration:underline;"> Good afternoon</h1>'
       
    )
