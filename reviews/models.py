from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.

RATE_SCORE = (
    (1, 'POOR'),
    (2, 'FAIR'),
    (3, 'AVARAGE'),
    (4, 'GREAT'),
    (5, 'EXCELLENT'),
)

class Review(models.Model):
    """
    Model representing a review.
    """
    user = models.ForeignKey('auth.User', related_name='reviewer', on_delete=models.CASCADE)
    description = CKEditor5Field('Description', config_name='default')
    title = models.CharField(max_length=80, null=False, blank=False)
    details = models.CharField(max_length=150, null=False, blank=False)
    rating = models.IntegerField(choices=RATE_SCORE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.title)