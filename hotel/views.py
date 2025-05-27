from django.shortcuts import render

# Create your views here.
"""
This file contains the views for the Hotel app.
"""
def about_view(request):
    return render(request, 'hotel/about.html')

def contact_view(request):
    return render(request, 'hotel/contact.html')

def error_404_view(request, exception):
    return render(request, 'hotel/404.html', status=404)