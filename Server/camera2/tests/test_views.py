from django.test import Client, TestCase
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index2_url = reverse('index2')

    def test_indexView_GET(self):
        response = self.client.get(self.index2_url)
        self.assertEquals(response.status_code, 200)
