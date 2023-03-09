from django.urls import path
from rest_framework import routers

from .views import TweetList, TweetDetail, FollowCreateAPIView, FollowDestroyAPIView
# router = routers.DefaultRouter()
# router.register(r'follow', UserFollowingViewSet)

urlpatterns = [
    path('',TweetList.as_view()),
    path('<int:pk>/', TweetDetail.as_view()),
    path('follow/', FollowCreateAPIView.as_view(), name='follow'),
    path('unfollow/<int:pk>/', FollowDestroyAPIView.as_view(), name='unfollow'),


]

# urlpatterns += router.urls