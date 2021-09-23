
from django.shortcuts import render, redirect

from ..models import  Customer
from django.contrib.auth.hashers import check_password
from django.views import View


class Login(View):
    error = None
    def get(self,request):
        return render(request, 'login.html')
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                request.session['email'] = customer.email

                return redirect('homepage')
            else:
                error = ("Email or password is invalid")
        else:
            error = ("Email or password is invalid")

        print(email, password)
        print(customer)
        return render(request, 'login.html', {'error': error})

def logout(request):
    request.session.clear()
    return redirect('login')