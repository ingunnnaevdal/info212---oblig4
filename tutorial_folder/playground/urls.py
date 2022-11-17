""""
We will map our urls here
"""
from django.urls import path
from . import views

# URLConf - model
urlpatterns = [
    path('hello/', views.say_hello),
    # always end a route with forward slash ( / )

]