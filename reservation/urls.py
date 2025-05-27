from django.urls import path
from .views import BookingsList, EditBookingView, DeleteBookingView, reservation_view
"""
This file contains the URL patterns for the Reservation app.
It maps URLs to views for making reservations, viewing bookings, editing bookings, and deleting bookings.
"""
urlpatterns = [
    path('make/', reservation_view, name='reservation'),
    path('my-bookings/', BookingsList.as_view(), name='bookings_list'),
    path('edit/<int:pk>/', EditBookingView.as_view(), name='editbooking'),
    path('delete/<int:pk>/', DeleteBookingView.as_view(), name='delete_booking'),
]
