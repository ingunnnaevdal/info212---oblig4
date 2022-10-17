#  mysite/views.py

from .models import Car
from rest_framework.response import Response
from .serializers import CarSerializer
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.http import HttpResponse


@api_view(['GET'])
def get_cars(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.data)
        return Response(serializer.data, status = status.HTTP_200_OK)
    else:
        return Response(serializer.data, status = status.HTTP_404_NOT_FOUND)

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


def say_hello(request):
    return HttpResponse("Hello World")