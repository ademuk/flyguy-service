import urllib2
from django.core import mail
from rest_framework.test import APILiveServerTestCase
from rest_framework import status
from BeautifulSoup import BeautifulSoup


class AuthTestCase(APILiveServerTestCase):

    def setUp(self):
        self.client.post('/api/users/', {
            'email': 'foo@bar.com',
            'password': 'foo',
            'first_name': 'foo',
            'last_name': 'bar'
        })

    def test_get_auth_token_fails(self):
        """Authentication fails if user e-mail is not confirmed"""
        response = self.client.post('/api/token-auth/', {
            'email': 'foo@bar.com',
            'password': 'foo'
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_auth_token(self):
        """Authentication passes with user with confirmed e-mail"""
        response = self.client.post('/api/token-auth/', {
            'email': 'foo@bar.com',
            'password': 'foo'
        })

        email = BeautifulSoup(mail.outbox[0].body)
        link = email.find('a', limit=1)

        # Load the confirmation link
        urllib2.urlopen(link.get('href'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)
