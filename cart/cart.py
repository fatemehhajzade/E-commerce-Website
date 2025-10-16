from shop.models import Product

class Cart:
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        self.cart = cart

    def add(self,product, quantity):
        product_id = str(product.id)
        product_qty = int(quantity)

        if product_id in self.cart:
            self.cart[product_id]['quantity'] += product_qty
        else:
            self.cart[product_id] = product_qty

        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_cart_products(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products

    def get_quantity(self):
        quantities = self.cart
        return quantities

    def get_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        total = 0

        for key, value in self.cart.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)

        return total

    def get_total_of_product(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        product_totals = {}

        for key, value in self.cart.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        product_totals[key] = product.sale_price * value
                    else:
                        product_totals[key] = product.price * value

        return product_totals


    def update(self,product,quantity):
        product_id = str(product.id)
        product_qty = int(quantity)

        ourcart = self.cart
        ourcart[product_id] = product_qty
        self.session.modified = True

        alaki = self.cart
        return alaki

    def delete(self,product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True
