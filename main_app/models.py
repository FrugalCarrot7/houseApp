from django.db import models
from django.forms import CharField, DateField, IntegerField

# Create your models here.

class House(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=50)
    size = models.PositiveIntegerField()

class Item(models.Model):
    name = models.CharField(max_length=50)
    date_purchase = models.DateField()
    price = models.IntegerField()
    description = CharField(max_length=200)


class Task(models.Model):
    name = models.CharField(max_length=50)
    due = models.DateField()
    instructions = models.CharField(max_length=500)

