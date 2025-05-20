from django.urls import path
from . import views
from .views import CreateReservation, ReservationList

urlpatterns = [
    path('', views.ReservationList.as_view(), name='reservation'),
    path('reservations/', CreateReservation.as_view(), name='create_reservation'),
]