from django.views.generic import ListView
from .models import Room  
"""
List view for rooms.
"""
class RoomListView(ListView):
    model = Room
    template_name = 'rooms/room_list.html' 
    context_object_name = 'rooms' 
