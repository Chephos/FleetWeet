from django.db import models
from django.conf import settings

from accounts.models import CustomUser

# Create your models here.

class Tweet(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='uploads/tweets/%Y/%m/%d', blank=True)
    author = models.ForeignKey(CustomUser, related_name='tweets', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text[:15]}...'