from .filters import add_flightFilter
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import Class
from .models import add_flight, Booking


def home(request):
    flights = add_flight.objects.all()
    searchFilter = add_flightFilter(request.GET, queryset=flights)

    context = {
        'flights': flights,
        'searchFilter': searchFilter,
    }
    return render(request, 'blogs/home.html', context)


def about(request):
    return render(request, 'blogs/about.html', {'title': 'About'})

def booking(request):
    return render(request, 'blogs/booking.html', {'title': 'Booking'})


def success(request):
    return render(request, 'blogs/success.html', {'title': 'Booking'})


class createmodelview(CreateView):
    model = Booking
    form_class = Class
    template_name = 'blogs/class.html'
    success_url = 'success.html'


def booked(request):
    Booked = Booking.objects.filter(user=request.user)
    Context = {
        'booked': Booked,
        'title': 'booked',
        'form': createmodelview,
    }
    return render(request, 'blogs/booked.html', Context)


def cancelBooking(request, Booking_id):
    toCancel = Booking.objects.get(id=Booking_id)
    toCancel.delete()
    return redirect(booked)

# Create your views here.

