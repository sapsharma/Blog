from unicodedata import name
from django.urls import path
from Blog_App import views

urlpatterns = [
    path('',views.home,name='home'),
    path('more_detail/<int:id>',views.more_detail,name='read_more'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('about',views.about,name='about'),
    path('contactus',views.contactus,name='contactus')

]
