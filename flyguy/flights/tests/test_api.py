from django.conf import settings
from django.core import mail
from django.test.utils import override_settings
from rest_framework.test import APILiveServerTestCase
from rest_framework import status


class UserTestCase(APILiveServerTestCase):

    def test_create_user(self):
        """Unauthentcated user can create new user"""
        response = self.client.post('/api/users/', {
            'email': 'foo@bar.com',
            'password': 'foo',
            'first_name': 'foo',
            'last_name': 'bar'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_required_fields(self):
        """first_name and last_name are required when creating a new user"""
        response = self.client.post('/api/users/', {
            'email': 'foo@bar.com',
            'password': 'foo'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_sends_confirmation_email(self):
        """"""
        response = self.client.post('/api/users/', {
            'email': 'foo@bar.com',
            'password': 'foo',
            'first_name': 'foo',
            'last_name': 'bar'
        })

        self.assertEqual(len(mail.outbox), 1)

        self.assertEqual(mail.outbox[0].subject, 'Email confirmation for foo@bar.com')


UserTestCase = override_settings(EMAIL_CONFIRM_LA_EMAIL_BACKEND=settings.EMAIL_BACKEND)(UserTestCase)
