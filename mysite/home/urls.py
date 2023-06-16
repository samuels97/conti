from django.urls import path
from . import  views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('contactus/', views.contactus, name='contactus'),
    path('login/', views.login, name='login'),
]