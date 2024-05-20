from django.contrib import admin
from django.urls import path,re_path

from app_category.views_api.categoryCRUD import *
urlpatterns = [
    path('all', CategoryList.as_view()),
    path('new', CategoryCreate.as_view()),
    path('info/<slug:category>', CategoryGet.as_view()),
    path('info/<slug:category>/update', CategoryUpdate.as_view()),
    path('info/<slug:category>/delete', CategoryDelete.as_view()),
]
