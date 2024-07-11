from django.shortcuts import render

# Create your views here.
def welcome_view(request):
    return render(request,'myapp/index.html')

def show_calc(request):
    return render(request, "myapp/calc.html")