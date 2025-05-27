from django.contrib import admin
from rooms.models import Room 
from reviews.models import Review
from .models import ContactMessage
from reservation.models import Reservation
# Register your models here.
"""
This file is used to register models with the Django admin site.
"""
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'room_type', 'price', 'created_at')
    list_filter = ['title']
"""
This class is used to customize the admin interface for the Room model.
It displays the title, user, room type, price, and creation date of each room.
"""
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'rating', 'created_at')
    list_filter = ['rating']
    search_fields = ('title', 'details')
    ordering = ('-created_at',)
    list_per_page = 10
"""
This class is used to customize the admin interface for the Review model.
It displays the title, user, rating, and creation date of each review.
It also allows filtering by rating and searching by title and details.
"""

admin.site.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    ordering = ('-created_at',)
    list_per_page = 10
"""
This class is used to customize the admin interface for the ContactMessage model.
It displays the name, email, and creation date of each contact message.
It also allows searching by name and email.
"""
admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'check_in', 'check_out', 'guests', 'room_type')
    search_fields = ('full_name', 'room_type')
    list_filter = ('check_in', 'check_out')
    ordering = ('-check_in',)
    list_per_page = 10