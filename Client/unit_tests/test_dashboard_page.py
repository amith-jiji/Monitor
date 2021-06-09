from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse


class TestProjectLoginPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='drivers/geckodriver.exe')
        self.browser.get(self.live_server_url + reverse('dashboard'))

    def tearDown(self):
        self.browser.close()

    def test_dashboard_page_css_property(self):
        self.assertEquals(self.browser.find_element_by_tag_name('body').value_of_css_property('background-color'), 'rgb(187, 186, 232)')

    def test_camera1_button(self):
        self.browser.find_element_by_id('camera1-button').click()
        self.assertEquals(
            self.browser.current_url, self.live_server_url + reverse('camera', args=[1])
        )

    def test_camera2_button(self):
        self.browser.find_element_by_id('camera2-button').click()
        self.assertEquals(
            self.browser.current_url, self.live_server_url + reverse('camera', args=[2])
        )

    def test_sign_out(self):
        self.browser.find_element_by_class_name('nav-link').click()
        self.assertEquals(
            self.browser.current_url, self.live_server_url+reverse('login')
        )
