from django.shortcuts import render, redirect

# Create your views here.

def Index(request):
    return render(request,"index.html")

def Magazine(request):
    return render(request,"magazine.html")

def Business(request):
    return render(request,"business.html")

def Sports(request):
    return render(request,"sports.html")

def Art(request):
    return render(request,"art.html")

def Politics(request):
    return render(request,"politics.html")

def Travel(request):
    return render(request,"travel.html")

def Contactus(request):
    return render(request,"contactus.html")