from django.contrib import admin
from django.urls import path,re_path

from app_car.views_api.carCRUD import *
urlpatterns = [
    path('all', CarList.as_view()),
    path('new', CarCreate.as_view()),
    path('info/<slug:brand>_<slug:model>_<slug:year>', CarGet.as_view()),
    path('info/<slug:brand>_<slug:model>_<slug:year>/update', CarUpdate.as_view()),
    path('info/<slug:brand>_<slug:model>_<slug:year>/delete', CarDelete.as_view()),
]
