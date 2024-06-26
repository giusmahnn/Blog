from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.title[:50]
    
    def get_absolute_url(self):
        return reverse("post_details", kwargs={'pk': self.pk})
