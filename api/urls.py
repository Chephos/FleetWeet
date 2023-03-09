from django.urls import path
from rest_framework import routers

from .views import TweetList, TweetDetail, FollowCreateAPIView,ProfileFeed,NewsFeed, FollowDestroyAPIView
# router = routers.DefaultRouter()
# router.register(r'follow', UserFollowingViewSet)

urlpatterns = [
    path('',TweetList.as_view()),
    path('<int:pk>/', TweetDetail.as_view()),
    path('follow/', FollowCreateAPIView.as_view(), name='follow'),
    path('unfollow/<int:pk>/', FollowDestroyAPIView.as_view(), name='unfollow'),
    path('profile-feed',ProfileFeed.as_view(), name='profile_feed'),
    path('news-feed', NewsFeed.as_view(), name='news_feed')


]

# urlpatterns += router.urls