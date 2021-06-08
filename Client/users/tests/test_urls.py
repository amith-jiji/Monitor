from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import loginView, logoutView, dashboardView, cameraView, reportView


class TestUrls(SimpleTestCase):

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, loginView)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logoutView)

    def test_dashboard_url_is_resolved(self):
        url = reverse('dashboard')
        self.assertEquals(resolve(url).func, dashboardView)

    def test_camera_url_is_resolved(self):
        url = reverse('camera', args=[1])
        self.assertEquals(resolve(url).func, cameraView)

    def test_report_url_is_resolved(self):
        url = reverse('report', args=[1])
        self.assertEquals(resolve(url).func, reportView)
