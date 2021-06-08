from django.test import Client, TestCase
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')

    def test_indexView_GET(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
