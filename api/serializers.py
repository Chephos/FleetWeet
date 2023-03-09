from rest_framework import serializers
from django.db import transaction
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model

from tweets.models import Tweet
from accounts.models import Follow


class FollowSerializer(serializers.ModelSerializer):
    follower = serializers.ReadOnlyField(source='follower.username')
    following = serializers.ReadOnlyField(source='following.username')
    

    class Meta:
        model = Follow
        fields = ('id','follower','following',)
        
class CustomUserSerializer(serializers.ModelSerializer):
    # followers = serializers.SerializerMethodField()
    # following = serializers.SerializerMethodField()
    follows = FollowSerializer()
    
    class Meta:
        model = get_user_model()
        fields = ['id','username','email','bio', 'follows',]
        extra_kwargs = {
            "password": {"write_only":True}
        }

    # def get_followers(self,obj):
    #     return FollowersSerializer(obj.followers.all(), many=True).data
    # def get_following(self,obj):
    #     return FollowingSerializer(obj.following.all(), many=True).data

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

# class FollowingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserFollowing
#         fields = ('id', 'following_user_id',)

# class FollowersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserFollowing
#         fields = ('id', 'follower_user_id',)

# class UserFollowingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserFollowing
#         fields = ('id','follower_user_id', 'following_user_id',)

