from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.

# FOLLOW_CHOICES = (
#     ('follow', 'Follow'),
#     ('unfollow', 'Unfollow')
# )

class CustomUser(AbstractUser):
    bio = models.CharField(max_length=160, default='')
    location = models.CharField(max_length=200, default='fleet_hq')
    # following = models.ManyToManyField("self", blank=True,
    #                                    related_name='followers',
    #                                    symmetrical=False)

    def __str__(self):
        return f"{self.username}"


class Follow(models.Model):
    follower = models.ForeignKey(get_user_model(),related_name='following',
                                on_delete=models.CASCADE)
    following = models.ForeignKey(get_user_model(), related_name='followers',
                                        on_delete=models.CASCADE)
    # action = models.CharField(choices=FOLLOW_CHOICES, max_length=10)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['follower','following'], name='unique_followers')
        ]
