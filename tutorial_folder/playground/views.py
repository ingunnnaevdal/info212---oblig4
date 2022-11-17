from cgitb import html
from django.shortcuts import render
from django.http import HttpResponse

# This is a request-handler

# Takes in a request and gives a response

# Create your views here.

def say_hello(request):
    return render(request, 'hello.html', {'name': 'Mosh'})

