from django.db import models

# Create your models here.
"""
This file contains the models for the Booking app.
It defines the ContactMessage model which is used to store messages from users.
The ContactMessage model includes fields for the user's name, email, message, and the date the message was created.
"""
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
