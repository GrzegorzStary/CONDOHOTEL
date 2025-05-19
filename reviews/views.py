from django.views.generic import CreateView
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin

class AddReview(LoginRequiredMixin, CreateView):
    """
    Add review view.
    """
    template_name = 'reviews/add_review.html'
    model = Review
    form_class = ReviewForm
    success_url = '/reviews'
    
    def form_valid(self, form):
        """
        If the form is valid, save the review and redirect to the success URL.
        """
        form.instance.user = self.request.user
        return super(AddReview, self).form_valid(form)