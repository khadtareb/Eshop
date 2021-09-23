from django.shortcuts import render, redirect

from ..models import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from ..models import Order
from ..middleware.auth import auth_middleware
from django.utils.decorators import method_decorator


class OrderView(View):

    @method_decorator(auth_middleware)
    def get(self, request):
        customer = request.session.get('customer')
        cart=request.session.get
        orders = Order.get_orders_by_customers(customer)
        print(orders,cart)
        return render(request, 'orders.html', {'orders': orders})
