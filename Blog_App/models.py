from email import message
from pyexpat import model
from django.db import models

# Create your models here.
class Blog_A(models.Model):
    Blog_Title=models.CharField(max_length=150)
    # Blog_Date=models.DateField(auto_now_add=True)
    Blog_Desc=models.TextField(max_length=500)
    Blog_Desc1=models.TextField(max_length=3000 , default='')

    Blog_Image=models.ImageField(upload_to='Image')


class Contactus(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500)