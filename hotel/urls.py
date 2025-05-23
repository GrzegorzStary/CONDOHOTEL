"""
URL configuration for hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from booking import urls as booking_urls
from .views import about_view, contact_view, error_404_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('', include(booking_urls), name='booking_urls'),
    path('rooms/', include('rooms.urls')),
    path('reviews/', include('reviews.urls')),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('reservation/', include('reservation.urls'), name='reservation_urls'),
    path('djrichtextfield/', include('djrichtextfield.urls')),
]
