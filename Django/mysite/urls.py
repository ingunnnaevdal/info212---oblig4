"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from .views import *
from .views import get_cars

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', get_cars),
    path('customers/', get_customers),
    path('save_car/', save_car),
    path('update_car/<int:id>', update_car),
    path('delete_car/<int:id>', delete_car),
    path('hello/', say_hello),
    path('form/', get_name), # Form for filling out information about user
    path('order_car/<int:customerID>/<int:carID>', order_car),
    #Customer mangler?
    #Employee mangler?
]


