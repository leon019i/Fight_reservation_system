from django import forms
from django.contrib.auth.models import User
from blog.models import Booking


class Class(forms.ModelForm):
    class Meta:
        model = Booking
        this_user = User
        fields = ['classes', 'price', 'user', 'flight']
