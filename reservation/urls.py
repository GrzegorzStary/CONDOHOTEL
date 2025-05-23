from django.urls import path
from . import views

urlpatterns = [
    path('reserve/', views.reservation_view, name='reservation'),
]
