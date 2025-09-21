from django.shortcuts import render,HttpResponse
from .models import Product

def helloworld(request):
    # return HttpResponse("<h1>سلام دنیا</h1>")

    # return render(request,'index.htm')

    # return render(request,'index.html')

    all_products = Product.objects.all()
    return render(request,'index.html',{'products':all_products})
    # return HttpResponse(all_products)

def about(request):
    return render(request,'about.html')