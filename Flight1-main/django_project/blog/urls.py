from django.urls import path

from . import views


urlpatterns = [

    path('about/', views.about, name='blog-about'),
    path('', views.home, name='blog-home'),
    path('booking/', views.booking, name='blog-booking'),
    path('booked/', views.booked, name='bolg-booked'),
    path('chooseClass/success.html', views.success, name='success'),
    path('chooseClass/', views.createmodelview.as_view(), name='chooseClass'),
    path('<int:Booking_id>/booked/', views.cancelBooking, name='cancelBooking'),

]
