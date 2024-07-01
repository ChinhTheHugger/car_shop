from django.contrib import admin
from django.urls import path,re_path

from app_brand.views_api.brandCRUD import *
urlpatterns = [
    path('all', BrandList.as_view()),
    path('new', BrandCreate.as_view()),
    path('info/<slug:brand>', BrandGet.as_view()),
    path('info/<slug:brand>/update', BrandUpdate.as_view()),
    path('info/<slug:brand>/delete', BrandDelete.as_view()),
]
