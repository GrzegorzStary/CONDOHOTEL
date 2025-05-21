from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReservationForm

@login_required
def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, "Your reservation has been made!")
            return redirect('reservation') 
    else:
        form = ReservationForm()
    
    return render(request, 'reservation/reservation_list.html', {'form': form})
