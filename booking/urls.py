from django.urls import path
from .views import Index, About, Contact, Error404



urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('404/', Error404.as_view(), name='404'),
]