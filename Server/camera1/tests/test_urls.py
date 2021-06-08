from django.test import SimpleTestCase
from django.urls import reverse, resolve
from camera1.views import indexView

class TestUrls(SimpleTestCase):

    def test_index1_url_is_resolved(self):
        url = reverse('index1')
        self.assertEquals(resolve(url).func, indexView)
