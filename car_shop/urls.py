"""
URL configuration for car_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    
    # path('api-auth/', include('rest_framework.urls')),
    
    # path('', include('app_main.urls')),
    # path('api/car/', include('app_car.urls')),
    # path('api/brand/', include('app_brand.urls')),
    # path('api/category/', include('app_category.urls')),
    # path('api/account/', include('app_account.urls')),
    # path('api/request/', include('app_request.urls')),
    # path('api/contract/', include('app_contract.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
