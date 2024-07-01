from django.contrib import admin
from django.urls import path,re_path

from app_request.views_api.requestCRUD import *
urlpatterns = [
    path('all', RequestList.as_view()),
    path('new', RequestCreate.as_view()),
    path('info/<slug:customer>', RequestGet.as_view()),
    path('info/<slug:customer>/update', RequestUpdate.as_view()),
    path('info/<slug:customer>/delete', RequestDelete.as_view()),
]
