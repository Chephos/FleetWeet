from rest_framework import generics, permissions,status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from tweets.models import Tweet
from accounts.models import Follow
from .serializers import TweetSerializer, FollowSerializer
from .permissions import IsAuthorOrReadOnly

userClass = get_user_model()
class TweetList(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class TweetDetail(generics.RetrieveDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

# class UserFollowingViewSet(viewsets.ModelViewSet):
#     permission_classes = (permissions.IsAuthenticated,)
#     serializer_class = UserFollowingSerializer
#     queryset = UserFollowing.objects.all()


# class AddFollower(APIView):
#     permission_classes = [permissions.IsAuthenticated,]

#     def post(self, request, format=None):
#         user = userClass.objects.get(follower_user_id=self.request.data.get('follower_user_id'))
#         follow = userClass.objects.get(follower_user_id=self.request.data.get('follow'))
#         UserFollowing.objects.create(follower_user_id=user.id,following_user_id=follow.id)
#         return JsonResponse({'status':status.HTTP_200_OK, 'data':"", 'message':"follow"+str(follow.follower_user_id)})

class FollowCreateAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self,request, format=None):
        follower = request.user
        following_pk = request.data.get('following')
        following = get_object_or_404(userClass, pk=following_pk)
       

        if follower == following:
            return Response({'detail':"You can't follow yourself, brudda."}, status=status.HTTP_400_BAD_REQUEST)
        
        
        follow, created = Follow.objects.get_or_create(follower=follower, following=following)
        if not created:
            return Response({'detail':f"You are already following {following.username}"}, status=status.HTTP_400_BAD_REQUEST)
        


        serializer = FollowSerializer(follow)
        return Response(serializer.data)

class FollowDestroyAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request, pk, format=None):
        follow = get_object_or_404(Follow, pk=pk)
        self.check_object_permissions(request, follow)
        follow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProfileFeed(generics.ListAPIView):
    serializer_class = TweetSerializer

    def get_queryset(self):
        """
        This view should return tweets written by the author only
        """
        user = self.request.user
        return Tweet.objects.filter(author=user)


class NewsFeed(generics.ListAPIView):
    serializer_class = TweetSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @method_decorator(cache_page(60*15))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        user = self.request.user
        my_followers = [follow.following for follow in user.following.all()]
        their_tweets = Tweet.objects.filter(author__in=my_followers).order_by('-created_on')
        return their_tweets
    