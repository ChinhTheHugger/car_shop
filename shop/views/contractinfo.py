from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from shop.models.car import Car
from shop.models.brand import Brand
from shop.models.account import Account
from shop.models.request import Request
from django.views import View
import codecs
from django.utils.encoding import force_bytes
from django.core.files.storage import FileSystemStorage
from upload_validator import FileTypeValidator
from django.core.files.uploadedfile import TemporaryUploadedFile
import mimetypes
from datetime import date

def get_contract(request,customerusername,brand,model,year):
    accountusername = request.session.get('account')
    customerinfo = Account.get_account_by_username_for_iterate(accountusername)