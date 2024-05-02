from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from shop.models.brand import Brand
from shop.models.account import Account
from django.views import View
import codecs
from django.utils.encoding import force_bytes
from django.core.files.storage import FileSystemStorage
from upload_validator import FileTypeValidator
from django.core.files.uploadedfile import TemporaryUploadedFile
import mimetypes

class AddNewContract(View):
    def get(self, request):
        customerusername = request.session.get('account')
        values = {
                'brand': "",
                'website': "",
                'desintext': "",
                'logo': ""
        }
        customerinfo = Account.get_account_by_username_for_iterate(customerusername)
        return render(request, 'addcontract.html', {'account': customerinfo, 'values': values})