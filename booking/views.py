from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib import messages
from .forms import ContactForm
from django.urls import reverse_lazy




class Index(TemplateView):
    template_name = 'booking/index.html'
    
class About(TemplateView):
    template_name = 'booking/about.html'

class ContactView(FormView):
    template_name = 'booking/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    
    def form_valid(self, form):
        form.save()  
        messages.success(self.request, "Thank you for contacting us. We will get back to you soon!")
        return super().form_valid(form)

    
class Error404(TemplateView):
    template_name = 'booking/404.html'

