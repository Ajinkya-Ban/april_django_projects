from django.contrib import admin
from . import models

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display =['job_title','desc']
admin.site.register(models.Job,JobAdmin)