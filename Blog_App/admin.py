from django.contrib import admin
from Blog_App.models import Blog_A,Contactus

# Register your models here.
@admin.register(Blog_A)
class Blog_B(admin.ModelAdmin):
    list_display=['Blog_Title','Blog_Desc','Blog_Desc1','Blog_Image']

@admin.register(Contactus)
class AdminContactus(admin.ModelAdmin):
    list_display=['name','email','subject','message']