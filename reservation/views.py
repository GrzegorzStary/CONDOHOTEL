from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReservationForm
from .models import Reservation 
from django.views.generic import DeleteView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
"""This file contains views for the reservation app.
It includes functionality for creating reservations, viewing bookings,
editing bookings, and deleting bookings.
"""
@login_required
def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, "Your reservation has been made!")
            return redirect('/reservations/my-bookings/') # Redirect to the bookings list after successful reservation
        form = ReservationForm()
    else:
        form = ReservationForm()
    return render(request, 'reservation/reservation_list.html', {'form': form})

class BookingsList(LoginRequiredMixin, ListView):
    model = Reservation 
    template_name = 'reservation/bookings_list.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReservationForm()
        return context

class EditBookingView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Reservation 
    template_name = 'reservation/edit_booking.html'
    form_class = ReservationForm
    success_url = '/reservations/my-bookings/'

    def test_func(self):
        booking = self.get_object()
        return booking.user == self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Your booking has been updated!")
        return super().form_valid(form)

class DeleteBookingView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Reservation 
    template_name = 'reservation/delete_booking.html'
    success_url = '/reservations/my-bookings/'

    def test_func(self):
        booking = self.get_object()
        return booking.user == self.request.user

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Your booking has been cancelled!")
        return super().delete(request, *args, **kwargs)
