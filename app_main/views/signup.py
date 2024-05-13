from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from shop.models.account import Account
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

        account = Account (username=username,
                             firstname=first_name,
                             lastname=last_name,
                             phone=phone,
                             email=email,
                             password=password,
                             type='customer')
        error_message = self.validateAccount (account)

        if not error_message:
            # print (first_name, last_name, phone, email, password)
            account.password = make_password (account.password)
            account.register ()
            return redirect ('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render (request, 'signup.html', data)

    def validateAccount(self, account):
        error_message = None
        if (not account.username):
            error_message = "Please Enter your Userame !!"
        elif len (account.username) < 3:
            error_message = 'Username must be 3 char long or more'
        if (not account.firstname):
            error_message = "Please Enter your First Name !!"
        elif len (account.firstname) < 3:
            error_message = 'First Name must be 3 char long or more'
        elif not account.lastname:
            error_message = 'Please Enter your Last Name'
        elif len (account.lastname) < 3:
            error_message = 'Last Name must be 3 char long or more'
        elif (not account.phone):
            error_message = 'Enter your Phone Number'
        elif len (account.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len (account.password) < 5:
            error_message = 'Password must be 5 char long'
        elif len (account.email) < 5:
            error_message = 'Email must be 5 char long'
        elif account.isExistEmail():
            error_message = 'Email Address Already Registered..'
        elif account.isExistUsername():
            error_message = 'Username Already Registered..'
        # saving

        return error_message
