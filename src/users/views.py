from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import  reverse
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    return render(request,"users/login.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password= request.POST["password"]
        user = authenticate(request,username=username,password=password)
        login(request,user)
        return render(request, "users/users.html")
    return render(request,"users/login.html",{
        "message":"Invalid credentials",
    })

    

def logout_view(request):
    logout(request)
    return render(request, "users/login.html")


###  TJzGKu#E-dws6p$
