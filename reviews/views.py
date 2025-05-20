from django.views.generic import CreateView, ListView
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin

class ReviewList(ListView):
    """
    List view for reviews.
    """
    model = Review
    template_name = 'reviews/reviews.html'
    context_object_name = 'reviews'
    
    def get_context_data(self, **kwargs):
        """
        Add additional context data to the template.
        """
        context = super(ReviewList, self).get_context_data(**kwargs)
        context['reviews'] = Review.objects.all()
        return context

class AddReview(LoginRequiredMixin, CreateView):
    """
    Add review view.
    """
    template_name = 'reviews/add_review.html'
    model = Review
    form_class = ReviewForm
    success_url = '/reviews/reviews/'
    
    def form_valid(self, form):
        """
        If the form is valid, save the review and redirect to the success URL.
        """
        form.instance.user = self.request.user
        return super(AddReview, self).form_valid(form)