from django.contrib import admin
from rooms.models import Room 
from reviews.models import Review
from .models import ContactMessage
# Register your models here.

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'room_type', 'price', 'created_at')
    list_filter = ['title']
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'rating', 'created_at')
    list_filter = ['rating']
    search_fields = ('title', 'details')
    ordering = ('-created_at',)
    list_per_page = 10
    

admin.site.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    ordering = ('-created_at',)
    list_per_page = 10
