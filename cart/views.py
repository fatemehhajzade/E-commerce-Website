from django.shortcuts import render, get_object_or_404
from .cart import Cart
from shop.models import Product
from django.http import JsonResponse


def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_cart_products()
    cart_items = []

    for product in cart_products:
        pid = str(product.id)
        item_data = cart.cart[pid]
        cart_items.append({
            'product': product,
            'quantity': item_data['quantity'],
            'total_price': int(item_data['quantity']) * int(item_data['price'])
        })

    return render(request, "cart_summary.html", {
        'cart_items': cart_items
    })

    # cart = Cart(request)
    # cart_products = cart.get_cart_products()
    # quantities = cart.cart  # داده‌های session (تعداد و قیمت)
    #
    # return render(request, "cart_summary.html", {
    #     'cart_products': cart_products,
    #     'quantities': quantities
    # })



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
    return render(request,"cart_summary.html",{})

def cart_update(request):
    return render(request,"cart_summary.html",{})

