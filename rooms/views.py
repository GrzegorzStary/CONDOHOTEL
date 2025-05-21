from django.views.generic import ListView
from .models import Room  # Adjust this import if your model is in a different app

class RoomListView(ListView):
    model = Room
    template_name = 'rooms/room_list.html' 
    context_object_name = 'rooms'  # lets use 'rooms' instead of 'object_list' in template
