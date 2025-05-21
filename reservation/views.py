# reservation/views.py
from django.views.generic import CreateView, ListView
from .models import Reservation
from django.urls import reverse_lazy
from datetime import date, timedelta
from django.shortcuts import render
from django.contrib import messages


class CreateReservation(CreateView):
    model = Reservation
    fields = ['name', 'email', 'check_in', 'check_out']
    template_name = 'reservation/reservation_form.html'
    success_url = reverse_lazy('reservation_list')

class ReservationList(ListView):
    model = Reservation
    template_name = 'reservation/reservation_list.html'

def room(request):
    today = date.today()
    tomorrow = today + timedelta(days=1)
    max_date = today + timedelta(days=365)

    context = {
        'todays_date': today.isoformat(),
        'tommorow': tomorrow.isoformat(),
        'max_date': max_date.isoformat(),
    }

    if request.method == 'POST':
        cin = request.POST.get('cin')
        cout = request.POST.get('cout')

        try:
            checkin = date.fromisoformat(cin)
            checkout = date.fromisoformat(cout)

            if checkin < today:
                messages.error(request, "Check-in date cannot be in the past.")
            elif checkout <= checkin:
                messages.error(request, "Check-out must be after check-in.")
            else:
                messages.success(request, "Dates are valid. Proceeding to check availability...")
                # context['rooms'] = get_available_rooms(checkin, checkout)
        except ValueError:
            messages.error(request, "Invalid date format. Please try again.")

    return render(request, 'booking/check_availability.html', context)
