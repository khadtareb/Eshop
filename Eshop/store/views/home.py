from django.shortcuts import render, redirect
from django.views import View
from ..models import Product, Category
from django.http import HttpResponse


# Create your views here.
class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        print(product)
        cart = request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product]=quantity-1
                else:
                    cart[product]=quantity+1
            else:
                cart[product] = 1
        else:
            cart={}
            cart[product] = 1
        request.session['cart'] = cart
        print('cart',request.session['cart'])
        return redirect('homepage')

    def get(self, request):
        # request.session.get('cart').clear()
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        print(request.GET)

        if categoryID:
            products = Product.get_product_by_categoryid(categoryID)
        else:
            products = Product.get_all_object()
        data = {}
        data['products'] = products
        data['categories'] = categories
        print('you are:', request.session.get('email'))
        # return render(request, 'orders/order.html', {'products': products})
        return render(request, 'index.html', data)

