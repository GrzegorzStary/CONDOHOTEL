from django.urls import path
from .views import Index



urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about/', Index.as_view(), name='about'),
    path('404/', Index.as_view(), name='404'),
]