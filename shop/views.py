from django.shortcuts import render,HttpResponse,redirect
from .models import Product,Category
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django import forms
from django.contrib import messages

def category_summary(request):
    all_category = Category.objects.all()
    return render(request, 'category_summary.html', {'categories':all_category})

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
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "رمز عبورها یکسان نیستند.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "این نام کاربری قبلاً ثبت شده است.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "این ایمیل قبلاً ثبت شده است.")
        else:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, 
                                            username=username, email=email, password=password1)
            # login(request, user)  # بعد از ثبت‌نام خودکار لاگین بشه
            messages.success(request, "ثبت‌نام با موفقیت انجام شد.")
            return redirect("home")

    return render(request, "signup.html")


def update_user(request):
    return render(request, "update_user.html")

def product(request,pk):
    product = Product.objects.get(id = pk)
    return render(request,'product.html',{'product':product})

def category(request,cat):
    cat = cat.replace("-"," ")
    try:
        category = Category.objects.get(name = cat)
        products = Product.objects.filter(category = category)
        return render(request,'category.html',{'products':products, 'category':category})
    except:
        messages.success(request, "دسته بندی وجود ندارد.")
        return redirect('home')

