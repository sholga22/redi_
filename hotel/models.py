import uuid

from django.db import models
from datetime import datetime


class Hotel(models.Model):
    hotel_name = models.CharField('Hotels name', max_length=50, help_text="Enter field name")
    qstars = models.CharField('How many stars', max_length=50)
    qfloor = models.IntegerField('Number of froors')
    qroom = models.IntegerField('How many rooms')
    hotel_Main_Img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.hotel_name


class Room(models.Model):
    num = models.IntegerField('Room number', help_text="")
    room_name = models.CharField('Room name', max_length=50, help_text="")
    view_from_the_window = models.CharField('View from the window', max_length=50, help_text="")
    price = models.CharField('Price', max_length=50, help_text="Enter field name")
    free = models.CharField('Free', max_length=50, help_text="Enter field name")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.room_name


class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.UUID, help_text="Unique ID for this person")
    first_name = models.CharField('First name', max_length=50, help_text="", blank=False)
    last_name = models.CharField('Last name', max_length=50, help_text="", blank=False)
    telefon = models.CharField('Telefon', max_length=50, help_text="")

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)



class Order(models.Model):
    order_num = models.IntegerField('Orders number', help_text="")
    id = models.UUIDField(primary_key=True, default=uuid.UUID, help_text="Unique ID for this order")
    Room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)
    date1 = models.DateTimeField(default=datetime.now, blank=False)
    date2 = models.DateTimeField(blank=False)
    person = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True)
    when_was_created =  models.DateTimeField(default=datetime.now, blank=False)


    def __str__(self):
        return self.order_num