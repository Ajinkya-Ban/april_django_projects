from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def welcome_view(request):
    try:
        finalans = 0
        data = {}
        # num1 = int(request.GET['n1'])
        # num2 = int(request.GET['n2'])
        # num1 = int(request.GET.get('n1'))
        # num2 = int(request.GET.get('n2'))

        if request.method == "POST":
            num1 = int(request.POST.get('n1'))
            num2 = int(request.POST.get('n2'))
            finalans = num1 + num2
       
            data = {
                "num1":num1,
                "num2":num2,
                "result":finalans
            }
            url = "/about-us/?result={}".format(finalans)
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,'myapp/index.html',data)
   

def show_calc(request):
    if request.method == "GET":
        result = request.GET.get('result')

    return render(request, "myapp/calc.html",{"result":result})