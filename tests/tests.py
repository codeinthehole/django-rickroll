import httplib
from django.test import TestCase
from django.test.client import Client
from django.conf import settings

class MiddlewareTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_raising_exception_issues_redirect(self):
        "Raising the HackingAttempt exception should lead to a redirect"
        response = self.client.get('/')
        self.assertEquals(httplib.FOUND, response.status_code)

    def test_raising_exception_redirects_to_youtube_by_default(self):
        "Raising the HackingAttempt exception should rickroll"
        response = self.client.get('/')
        self.assertEquals('http://www.youtube.com/watch?v=oHg5SJYRHA0', response['Location'])

    def test_redirect_url_can_be_manually_set(self):
        "The redirect URL can be changed in settings"
        settings.RICKROLL_URL = 'http://www.youtube.com/watch?v=YbaTur4A1OU'
        response = self.client.get('/')
        self.assertEquals(settings.RICKROLL_URL, response['Location'])
