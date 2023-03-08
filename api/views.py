from rest_framework import generics, permissions

from tweets.models import Tweet
from .serializers import TweetSerializer
from .permissions import IsAuthorOrReadOnly

class TweetList(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class TweetDetail(generics.RetrieveDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)