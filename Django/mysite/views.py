#  mysite/views.py

from .models import Car
from. models import Customer
from rest_framework.response import Response
from .serializers import CarSerializer, CustomerSerializer
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .forms import NameForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
import pdb


@api_view(['GET'])
def get_cars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def save_car(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def update_car(request, id):
    try:
        theCar = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    serializer = CarSerializer(theCar, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_car(request, id):
    try:
        theCar = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    theCar.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_customers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def save_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def order_car(request, customerID, carID):
    try:
        car = Car.objects.get(pk=carID)
        customer = Customer.objects.get(pk=customerID)
    except Car.DoesNotExist or Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if customer.status == True: #customer has ordered another car
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif car.status == 'available' or car.status == 'Available':
        car.status = "booked"
        customer.status = True
        customer.ordered_car = carID
    car_serializer = CarSerializer(car)
    customer_serializer = CustomerSerializer(customer)
    return Response(car_serializer.data, customer_serializer.data, status = status.HTTP_200_OK)

def say_hello(request):
    return HttpResponse("Hello World")


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

# ------------------------------------------------------------------------
