import urllib2
from django.conf import settings
from django.core import mail
from django.test.utils import override_settings
from rest_framework.test import APILiveServerTestCase
from rest_framework import status
from BeautifulSoup import BeautifulSoup


class AuthTestCase(APILiveServerTestCase):

    def setUp(self):
        test_url = self.live_server_url.replace('http://', '')
        with self.settings(EMAIL_CONFIRM_LA_DOMAIN=test_url):
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

        email = BeautifulSoup(mail.outbox[0].body)
        link = email.find('a')
        # Load the confirmation link
        urllib2.urlopen(link.get('href'))

        response = self.client.post('/api/token-auth/', {
            'email': 'foo@bar.com',
            'password': 'foo'
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)


AuthTestCase = \
    override_settings(EMAIL_CONFIRM_LA_EMAIL_BACKEND=settings.EMAIL_BACKEND)(AuthTestCase)
