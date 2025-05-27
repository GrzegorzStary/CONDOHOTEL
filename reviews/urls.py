from django.urls import path
from .views import AddReview, ReviewList
"""
This file contains the URL patterns for the Reviews app.
It maps URLs to views for adding reviews and listing reviews.
"""
urlpatterns = [
    path('', AddReview.as_view(), name='add_review'),
    path('reviews/', ReviewList.as_view(), name='reviews'),
]