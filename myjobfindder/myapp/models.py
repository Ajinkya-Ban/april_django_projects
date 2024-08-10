from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Job(models.Model):
    job_title = models.CharField(max_length = 150)
    desc = HTMLField()
    
    def __str__(self):
        return self.job_title