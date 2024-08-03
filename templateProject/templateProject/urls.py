
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.welcome_view,name="home"),
    path('about-us/', views.show_calc,name="about"),
    path('submitans/', views.submitans, name="submitans"),
]
