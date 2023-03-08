from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    bio = models.CharField(max_length=160, default='')
    location = models.CharField(max_length=200, default='fleet_hq')
    following = models.ManyToManyField("self", blank=True,
                                       related_name='followers',
                                       symmetrical=False)

    def __str__(self):
        return f"{self.username}"