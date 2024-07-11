from django.shortcuts import render

# Create your views here.
def show_index(request):
    return render(request,'myapp/index.html')