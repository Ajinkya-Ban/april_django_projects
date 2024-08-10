from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length = 150)
    prod_info = models.TextField()
    prod_img = models.ImageField(upload_to='media/prod_imgs/')

    
    def __str__(self):
        return self.title
        
    class Meta():
        verbose_name_plural = "Product"

class SliderProd(models.Model):
    title = models.CharField(max_length = 150)
    slider_photo= models.ImageField(upload_to='media/slider')

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length = 150)
    company = models.CharField(max_length = 150)
    email = models.CharField(max_length = 150)
    phone = models.CharField(max_length = 150)
    message = models.TextField()

    def __str__(self):
        return self.name
    
    
    