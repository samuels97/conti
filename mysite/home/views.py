from django.shortcuts import render

def contactus(request):
    return render(request, "home/contactus.html", {})

def register(request):
    return render(request, "home/register.html", {})