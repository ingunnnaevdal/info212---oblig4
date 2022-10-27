#  mysite/views.py

from .models import Car, Customer, Employee
from rest_framework.response import Response
from .serializers import CarSerializer, CustomerSerializer
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view

customerbookedcar = {}

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
def get_customer(request):
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer, many=True)
    print(serializer.data)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def save_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def update_customer(request, id):
    try:
        theCustomer = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    serializer = CustomerSerializer(theCustomer, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_customer(request, id):
    try:
        theCustomer = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    theCustomer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


#Funker sett bort fra at det ikke blir lagret at car er booked
@api_view(['GET'])
def order_car(request, customerID, carID):
    global customerbookedcar
    try:
        car = Car.objects.get(pk=carID)
        customer = Customer.objects.get(pk=customerID)
    except Car.DoesNotExist or Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if customer.id in customerbookedcar:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if car.status == 'available' or car.status == 'Available':
        car.status = "booked"
        customerbookedcar.update({customer.id : car.id})
    car_serializer = CarSerializer(car)
    return Response(car_serializer.data, status = status.HTTP_200_OK)