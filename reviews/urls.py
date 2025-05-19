from django.urls import path
from .views import AddReview, ReviewList

urlpatterns = [
    path('', AddReview.as_view(), name='add_review'),
    path('reviews/', ReviewList.as_view(), name='reviews'),
]