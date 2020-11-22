from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from app1.models import  Product
from .forms import Register
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout


def homepage(request):
    data = Product.objects.all()
    cart = request.COOKIES
    lcart = len(request.COOKIES)
    y = 0
    for x, y in cart.items():
        y += y
    tp = y

    if request.user:
        srng = request.user
        return render(request,"home.html",{"srng":srng,"data":data,"lcart":lcart,"cart":cart,"tp":tp})
    else:
        return render(request, "home.html",{"data":data,"lcart":lcart,"cart":cart,"tp":tp})


def userlogin(request):
    cart = request.COOKIES
    lcart = len(request.COOKIES)
    y = 0
    for x, y in cart.items():
        y += y
    tp = y

    if request.method == "POST":

        fm = AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
            return render(request,"profile.html",{"name":request.user})
    else:
        if request.user.is_authenticated:
            name = request.user
            print(name)
            return render(request, "profile.html", {"name": name,"lcart":lcart,"cart":cart,"tp":tp})
        else:
            fm = AuthenticationForm()
            return render(request,"login.html",{'form':fm,"lcart":lcart,"cart":cart,"tp":tp})


def register(request):
    cart = request.COOKIES
    lcart = len(request.COOKIES)
    y = 0
    for x, y in cart.items():
        y += y
    tp = y

    if request.method == "POST":
        fm = Register(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/login/")
    else:
        fm = Register()
    return render(request, "register.html",{'form':fm,"lcart":lcart,"cart":cart,"tp":tp})


def forgotpassword(request):
    return None

def smartphone(request):
    data = Product.objects.all()
    cart = request.COOKIES
    lcart = len(request.COOKIES)
    y = 0
    for x, y in cart.items():
        y += y
    tp = y


    data = Product.objects.filter(Category="Mobile")

    if request.user:
        srng = request.user
        return render(request, "smartphone.html",{"data":data,"srng":srng,"lcart":lcart,"cart":cart,"tp":tp})

    return render(request, "smartphone.html",{"data":data,"lcart":lcart,"cart":cart,"tp":tp})


def laptop(request):
    cart = request.COOKIES
    lcart = len(request.COOKIES)
    y = 0
    for x, y in cart.items():
        y += y
    tp = y


    data = Product.objects.filter(Category="Laptop")

    if request.user:
        srng = request.user
        return render(request,"laptop.html",{"data":data,"srng":srng,"lcart":lcart,"cart":cart,"tp":tp})

    return render(request,"laptop.html",{"data":data,"lcart":lcart,"cart":cart,"tp":tp})


def camera(request):
    cart = request.COOKIES
    lcart = len(request.COOKIES)
    y = 0
    for x, y in cart.items():
        y += y
    tp = y


    data = Product.objects.filter(Category="Camera")

    if request.user:
        srng = request.user
        return render(request,"camera.html",{"data":data,"srng":srng,"lcart":lcart,"cart":cart,"tp":tp})

    return render(request,"camera.html",{"data":data,"lcart":lcart,"cart":cart,"tp":tp})

def profile(request):
    cart = request.COOKIES
    lcart = len(request.COOKIES)
    y = 0
    for x, y in cart.items():
        y += y
    tp = y


    if request.user.is_authenticated:
        name=request.user
        print(name)
        return render(request,"profile.html",{"name":name,"lcart":lcart,"cart":cart,"tp":tp})
    else:
        return redirect('login')

def userlogout(request):
    logout(request)
    return redirect('login')


def addtocart(request):

    try:
        name = request.GET.get("name")
        price = request.GET.get("price")
        response = HttpResponse("Cookie_Set")

        data = response.set_cookie(name ,price)

        return response

    except :

        return redirect('laptop')


















