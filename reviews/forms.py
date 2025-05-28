from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form for creating and updating reviews.
    """
    class Meta:
        model = Review
        fields = ['title', 'details', 'rating']
        title = forms.CharField(max_length=300, required=True)
        details = forms.CharField(widget=RichTextWidget, required=True)
        rating = forms.ChoiceField(required=True)
        widgets = {
            'details': forms.Textarea(attrs={'rows': 5}),
        }
        labels = {
            'title': 'Title',
            'details': 'Details',
            'rating': 'Rating',
        }
