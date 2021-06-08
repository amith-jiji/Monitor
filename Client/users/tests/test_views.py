from django.test import Client, TestCase
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.dashboard_url = reverse('dashboard')
        self.camera_url = reverse('camera', args=[1])
        self.report_url = reverse('report', args=[1])

    def test_indexView_GET(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_logoutView_GET(self):
        response = self.client.get(self.logout_url)
        self.assertRedirects(response, expected_url=self.login_url, status_code=302, target_status_code=200,
                             fetch_redirect_response=True)

    def test_dashboardView_GET(self):
        response = self.client.get(self.dashboard_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')

    def test_CameraView_GET(self):
        response = self.client.get(self.camera_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'camera.html')
