from rest_framework import serializers

from tweets.models import Tweet
from accounts.models import CustomUser



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username','email','bio']

class TweetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tweet
        fields = ['id','text','image','author', 'created_on',]
        read_only_fields = ['author']