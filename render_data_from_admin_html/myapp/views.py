from django.shortcuts import render
from myapp.models import *
# Create your views here.

def indexPage(request):
    productData = Products.objects.all().order_by('-title')[:3]
    sliderData = SliderProd.objects.all()

    data = {
        "pData":productData,
        "slider":sliderData
    }
    return render(request,"myapp/index.html",data)

def contact(request):
    if request.method =='POST':
        pname = request.POST.get('name')
        pcompany = request.POST.get('company')
        pemail = request.POST.get('email')
        pphone= request.POST.get('phone')
        pmessage = request.POST.get('message')

        pass_data = Contact(name = pname,company=pcompany,email=pemail,phone=pphone,message=pmessage)
        pass_data.save()
        
    return render(request,"myapp/contact.html")