from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import datetime
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from tweets.models import Tweet
from accounts.models import CustomUser

# Create your tests here.
User = get_user_model()
class TweetTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123', email='testuser1@email.com',
            

        )
        testuser1.save()

        # create a tweet
        test_tweet = Tweet.objects.create(
            author=testuser1,text='dummy text',image='some/image/url/path',
            created_on=datetime.now()
        )
        test_tweet.save()

    def test_tweet_content(self):
        tweet = Tweet.objects.get(id=1)
        author = f'{tweet.author}'
        text = f'{tweet.text}'
        image = f'{tweet.image}'
        created_on = tweet.created_on
        self.assertEqual(author, 'testuser1')
        self.assertEqual(text, 'dummy text')
        self.assertEqual(image, 'some/image/url/path')
        self.assertIs(type(created_on), datetime)

    def test_tweet_object_name_is_some_text_with_three_dots(self):
        tweet = Tweet.objects.get(pk=1)
        expected_object_name = f"{tweet.text[:15]}..."
        self.assertEqual(str(tweet), expected_object_name)


# class AccountTestCase(APITestCase):
#     def test_create_account(self):
#         """
#         Ensure we can create a new account object
#         """
#         url = '/api/v1/registration/'
#         data = {
#                 'username':'some name',
#                 'email':'some@email.com',
#                 'password1':'some password',
#                 'password2':'some password',
#                 'bio':'some bio',
#                 'location':'some location',
#                 }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(CustomUser.objects.count(), 1)
#         self.assertEqual(CustomUser.objects.get().username, 'some name')

# class FollowTestCase(APITestCase):
#     def test_follow_user(self):
#         """
#         Ensure we can create a new follow object
#         """

#         url = reverse('follow')
#         data = {
#             'follower':1,
#             'following':2,
#         }
#         response = self.client.post(url,data,format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)