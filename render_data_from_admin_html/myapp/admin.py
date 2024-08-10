from django.contrib import admin
from . import models
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','prod_info','prod_img']
admin.site.register(models.Products, ProductAdmin)

class SliderAdmin(admin.ModelAdmin):
    list_display = ['title','slider_photo']
admin.site.register(models.SliderProd,SliderAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','company','email','phone','message']
admin.site.register(models.Contact,ContactAdmin)

