from django.shortcuts import render

def home(request):
    return render(request, "home/home.html", {})

def contactus(request):
    return render(request, "home/contactus.html", {})

def register(request):
    return render(request, "home/register.html", {})

def login(request):
    return render(request, "home/login.html", {})