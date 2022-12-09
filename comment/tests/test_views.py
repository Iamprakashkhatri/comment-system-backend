import json
from rest_framework import status
from django.test import TestCase, Client
from user.models import User
from django.urls import reverse
from ..models import *
from ..serializers import *


# initialize the APIClient app
client = Client()

class GetAllCommentsTest(TestCase):
    """Test module for GET all comments  API"""

    def setUp(self):
        self.user_first = User.objects.create_user(
            username='test test',
            password='test')

        client.force_login(self.user_first)

        self.comment_first=Comment.objects.create(
            user=self.user_first,description="this is description")

        self.comment_second=Comment.objects.create(
            user=self.user_first,description="this is description for comment second")

        self.reply_first=Reply.objects.create(
            user=self.user_first,description="this is description",comment=self.comment_first)
    
    def test_get_all_comments(self):
        response = client.get(reverse('comment:comments-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['description'], self.comment_first.description)


class CreateIndividualCommentTest(TestCase):
    """Test module for Create individual Comment API"""

    def setUp(self):

        self.user_first = User.objects.create_user(
            username='test test',
            password='test')

        client.force_login(self.user_first)

        self.valid_payload={
            'user':self.user_first.id,
            'description': 'this is test',
        }
        self.invalid_payload={
            'description': ''
        }

    def test_valid_create_individual_comment_with_pk(self):
        response = client.post(
            reverse('comment:comments-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['data']['description'], 'this is test')

    def test_invalid_create_individual_comment_with_pk(self):
        response = client.post(
            reverse('comment:comments-list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CreateIndividualReplyTest(TestCase):
    """Test module for Create individual reply API"""

    def setUp(self):

        self.user_first = User.objects.create_user(
            username='test test',
            password='test')

        self.comment_first=Comment.objects.create(
            user=self.user_first,description="this is description")

        client.force_login(self.user_first)

        self.valid_payload={
            'user':self.user_first.id,
            'comment':self.comment_first.id,
            'description': 'this is test',
        }
        self.invalid_payload={
            'description': ''
        }

    def test_valid_create_individual_reply_with_pk(self):
        response = client.post(
            reverse('comment:reply-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['data']['description'], 'this is test')

    def test_invalid_create_individual_reply_with_pk(self):
        response = client.post(
            reverse('comment:reply-list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

