from django.urls import path
from .views import AddReview

urlpatterns = [
    path('', AddReview.as_view(), name='add_review'),
]