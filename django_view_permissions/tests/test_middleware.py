"""
Tests the functionality of middleware.
"""
from django.test.testcases import TestCase
from django.urls import reverse


class MiddlewareTestCase(TestCase):
    """
    View Permission Middleware Tests
    """
    def setUp(self):
        super(MiddlewareTestCase, self).setUp()
        self.test_url = reverse('test')

    def test_dummy(self):
        """ A Dummy Test """
        response = self.client.get(self.test_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode('utf-8'), 'ok')
