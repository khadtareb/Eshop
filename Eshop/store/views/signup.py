from django.shortcuts import render, redirect

from ..models import Customer
from django.contrib.auth.hashers import make_password
from django.views import View
class Signup(View):
    def validation(self,customer):
        error = None
        if not customer.first_name:
            error = "first name required"
        elif len(customer.first_name) < 4:
            error = "first name should be atleast length 4"
        if not customer.last_name:
            error = "last name required"
        elif len(customer.last_name) < 5:
            error = "last name should be atleast length 5"
        if not customer.phone:
            error = "phone no required"
        elif len(customer.phone) < 10:
            error = "phone should be atleast length 10"
        if not customer.password:
            error = "password required"
        elif len(customer.password) < 6:
            error = "password should be atleast length 6"
        if not customer.email:
            error = "Email required"
        elif len(customer.email) < 6:
            error = "email should be atleast length 6"

        elif customer.isExists():
            error = "Email already exists"

        return error

    def get(self,request):
        return render(request, 'signup.html')
    def post(self,request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        values = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error = None

        # return HttpResponse("account created")

        # validation

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password, )
        error = self.validation(customer)
        if not error:
            print(first_name, last_name, phone, email)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error,
                'values': values,
            }
            return render(request, 'signup.html', data)
