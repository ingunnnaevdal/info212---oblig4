from rest_framework import serializers
from .models import Car, Customer

"""
In this file we describe the process of transforming a python object to JSON
"""

"""

class CarSerializer(
    serializers.ModelSerializer):  # In the ModelSerializer class, we have a metadata describing the model.
    class Meta:
        model = Car
        fields = ['id', 'make', 'carmodel']

"""

"""
Serializers package and unpack data when it goes between servers and databases.
"""



class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'carmodel', 'year', 'location', 'status']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'address', 'age', 'status', 'ordered_car']
        

