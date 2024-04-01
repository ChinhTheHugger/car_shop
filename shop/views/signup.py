from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from shop.models.customer import Customer
from django.views import View


class Signup (View):
    def get(self, request):
        return render (request, 'signup.html')

    def post(self, request):
        postData = request.POST
        username = postData.get('username')
        first_name = postData.get ('firstname')
        last_name = postData.get ('lastname')
        phone = postData.get ('phone')
        email = postData.get ('email')
        password = postData.get ('password')
        # validation
        value = {
            'username': username,
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer (customerusername=username,
                             firstname=first_name,
                             lastname=last_name,
                             phone=phone,
                             email=email,
                             password=password)
        error_message = self.validateCustomer (customer)

        if not error_message:
            print (first_name, last_name, phone, email, password)
            customer.password = make_password (customer.password)
            customer.register ()
            return redirect ('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render (request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.customerusername):
            error_message = "Please Enter your Userame !!"
        elif len (customer.customerusername) < 3:
            error_message = 'Username must be 3 char long or more'
        if (not customer.firstname):
            error_message = "Please Enter your First Name !!"
        elif len (customer.firstname) < 3:
            error_message = 'First Name must be 3 char long or more'
        elif not customer.lastname:
            error_message = 'Please Enter your Last Name'
        elif len (customer.lastname) < 3:
            error_message = 'Last Name must be 3 char long or more'
        elif not customer.phone:
            error_message = 'Enter your Phone Number'
        elif len (customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len (customer.password) < 5:
            error_message = 'Password must be 5 char long'
        elif len (customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExistEmail():
            error_message = 'Email Address Already Registered..'
        elif customer.isExistUsername():
            error_message = 'Username Already Registered..'
        # saving

        return error_message
