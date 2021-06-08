from django.test import SimpleTestCase
from django.urls import reverse, resolve
from feed.views import indexView

class TestUrls(SimpleTestCase):

    def test_index1_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, indexView)
