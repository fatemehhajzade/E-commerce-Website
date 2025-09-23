from django.shortcuts import render,HttpResponse,redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def helloworld(request):
    # return HttpResponse("<h1>سلام دنیا</h1>") 

    # return render(request,'index.htm')

    # return render(request,'index.html')

    all_products = Product.objects.all()
    return render(request,'index.html',{'products':all_products})
    # return HttpResponse(all_products)

def about(request):
    return render(request,'about.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, ("Logged in successfully!"))
            return redirect("home")
        else:
            messages.success(request, ("Error!"))
            return redirect("login")
    else:
        return render(request,'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ("Logged out successfully!"))
    return redirect("home")

def signup_user(request):
    if request.method == "POST":
        username = request.POST.get['username']
        email = request.POST.get['email']
        password1 = request.POST.get['password']
        password2 = request.POST.get['password']


        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, ("Logged in successfully!"))
            return redirect("home")
        else:
            messages.success(request, ("Error!"))
            return redirect("login")
    else:
        return render(request,'login.html')
