from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from shop.models.account import Account
from django.views import View


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get ('return_url')
        return render (request, 'login.html')

    def post(self, request):
        username = request.POST.get ('username')
        password = request.POST.get ('password')
        cus = Account.get_account_by_username(username)
        error_message = None
        if cus:
            flag = check_password (password,cus.password)
            if flag:
                request.session['account'] = cus.username

                if Login.return_url:
                    return HttpResponseRedirect (Login.return_url)
                else:
                    Login.return_url = None
                    return redirect ('homepage')
            else:
                error_message = 'Wrong password !!'
        else:
            error_message = 'No such username !!'

        print (username, password)
        return render (request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')
