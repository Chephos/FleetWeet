from rest_framework import serializers
from django.db import transaction
from dj_rest_auth.registration.serializers import RegisterSerializer

from tweets.models import Tweet
from accounts.models import CustomUser



# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['id','username','email','bio']

class CustomRegisterSerializer(RegisterSerializer):
    bio = serializers.CharField(max_length=160, default='')
    location = serializers.CharField(max_length=200, default='fleet_hq')
    
    @transaction.atomic
    def save(self,request):
        user = super().save(request)
        user.bio = self.data.get('bio')
        user.location = self.data.get('location')
        user.save()
        return user

class TweetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tweet
        fields = ['id','text','image','author', 'created_on',]
        read_only_fields = ['author']