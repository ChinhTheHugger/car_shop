from django.contrib import admin
from django.urls import path,re_path

from app_contract.views_api.contractCRUD import *
urlpatterns = [
    path('all', ContractList.as_view()),
    path('new', ContractCreate.as_view()),
    path('info/<slug:customer>', ContractGet.as_view()),
    path('info/<slug:customer>/update', ContractUpdate.as_view()),
    path('info/<slug:customer>/delete', ContractDelete.as_view()),
]
