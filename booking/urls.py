from django.contrib import admin
from django.urls import path
from booking import views as booking_views


urlpatterns = [
	path('admin/', admin.site.urls),
	path('', booking_views.index, name='index'),
]