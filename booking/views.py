from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'booking/index.html'
    
class About(TemplateView):
    template_name = 'booking/about.html'
    
class Contact(TemplateView):
    template_name = 'booking/contact.html'
    
class Error404(TemplateView):
    template_name = 'booking/404.html'

