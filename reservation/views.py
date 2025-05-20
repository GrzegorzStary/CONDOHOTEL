# reservation/views.py
from django.views.generic import CreateView, ListView
from .models import Reservation
from django.urls import reverse_lazy


class CreateReservation(CreateView):
    model = Reservation
    fields = ['name', 'email', 'check_in', 'check_out']
    template_name = 'reservation/reservation_form.html'
    success_url = reverse_lazy('reservation_list')

class ReservationList(ListView):
    model = Reservation
    template_name = 'reservation/reservation_list.html'
