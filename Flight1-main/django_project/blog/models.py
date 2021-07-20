from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import forms
from aircraft.models import AddAirCraft


class add_flight(models.Model):
    source = models.CharField(max_length=100)
    To = models.CharField(max_length=100)
    check_in_date = models.DateTimeField(default=timezone.now)
    check_out_date = models.DateTimeField(default=timezone.now)
    author = models.CharField(default='Admin', max_length=10)
    no_of_tickets = models.DecimalField(default=100, max_digits=3, decimal_places=0)
    plane = models.ForeignKey(AddAirCraft, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str('From : '+self.source)+str(' To : '+self.To)


# class Booking(models.Model):
#     source = models.CharField(max_length=100)
#     To = models.CharField(max_length=100)
#     check_in_date = models.DateTimeField(default=timezone.now)
#     check_out_date = models.DateTimeField(default=timezone.now)
#     no_of_avilable_tickets = models.DecimalField(default=100, max_digits=3, decimal_places=0)
#     class_avaiable = models.DecimalField(default=3, max_digits=1, decimal_places=0)
#     no_of_booked_tickets = models.DecimalField(default=0, max_digits=2, decimal_places=0, max_value=20)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
# Create your models here.
Class = [('economey', 'economey'), ('first', 'first'), ('luxury', 'luxury'), ('premium', 'premium')]


class Booking(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    flight = models.ForeignKey(add_flight, null=False, on_delete=models.CASCADE)
    classes = models.CharField(max_length=10, choices=Class, default='economey')
    price = models.DecimalField(default=600, decimal_places=0, max_digits=5)

    def __str__(self):
        return str(self.user) + str(self.flight)
