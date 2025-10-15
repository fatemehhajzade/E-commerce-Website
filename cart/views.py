from django.shortcuts import render, get_object_or_404
from .cart import Cart
from shop.models import Product
from django.http import JsonResponse


def cart_summary(request):

    cart = Cart(request)
    cart_products = cart.get_cart_products()
    quantities = cart.get_quantity()

    return render(request, "cart_summary.html", {
        'cart_products': cart_products,
        'quantities': quantities
    })


def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))  # ✅ تعداد محصول
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)  # 👈 پاس دادن مقدار تعداد

    # response = JsonResponse({'Product Name': product.name}
    cart_quantity = cart.__len__()
    response = JsonResponse({'qty': cart_quantity})
    return response

def cart_delete(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        cart.delete(product=product_id)
        response = JsonResponse({'product': product_id})
        return response

def cart_update(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))  # ✅ تعداد محصول
        product = get_object_or_404(Product, id=product_id)

        cart.update(product=product, quantity=product_qty)
        response = JsonResponse({'qty': product_qty})
        return response

