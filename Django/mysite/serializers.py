from rest_framework import serializers

from .models import Car, Employee, Customer


"""
In this file we describe the process of transforming a python object to JSON
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
        fields = ['id', 'name', 'address', 'age']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["name", "address", "branch"]
