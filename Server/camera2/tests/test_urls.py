from django.test import SimpleTestCase
from django.urls import reverse, resolve
from camera2.views import indexView

class TestUrls(SimpleTestCase):

    def test_index2_url_is_resolved(self):
        url = reverse('index2')
        self.assertEquals(resolve(url).func, indexView)
