from unittest.util import _MAX_LENGTH
from xmlrpc.client import Boolean
from django.db import models

class Car(models.Model):
    make = models.CharField(max_length= 50)
    carmodel = models.CharField(max_length= 50)
    year = models.PositiveIntegerField()
    location = models.CharField(max_length = 50)
    status = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.make} {self.carmodel} {self.year} {self.location} {self.status}"

class Employee(models.Model):
    name = models.CharField(max_length= 50)
    address = models.CharField(max_length= 50)
    branch = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.name} {self.address} {self.branch}"


class Customer(models.Model):
    name = models.CharField(max_length= 50)
    address = models.CharField(max_length= 50)
    age = models.PositiveIntegerField()
    status = models.BooleanField(default = False) #True if the customer has ordered a car
    ordered_car = models.PositiveIntegerField(default = 0) #regner med ingen biler har id=0?

    def __str__(self):
        return f"{self.name} {self.address} {self.age} {self.status} {self.ordered_car}"
    

    # make and model are attributes where we can store strings.
    # The __str__ method just tells Django what to print when it
    # needs to print out an instance of the carmodel

