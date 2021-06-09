from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse


class TestProjectLoginPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='drivers/geckodriver.exe')
        self.browser.get(self.live_server_url + reverse('camera', args=[1]))

    def tearDown(self):
        self.browser.close()

    def test_camera_page_css_property(self):
        self.assertEquals(self.browser.find_element_by_class_name('box').value_of_css_property('flex-direction'),
                          'column')

    def test_camera_page_text(self):
        self.assertEquals(self.browser.find_element_by_id('camera-text').text, 'Live Stream')

    def test_camera_stream(self):
        self.assertEquals(self.browser.find_element_by_class_name('stream').get_attribute('src'),
                          'http://127.0.0.1:8000/camera1')

    def test_camera_map_css(self):
        self.assertEquals((self.browser.find_element_by_id('map').value_of_css_property('height'),
                           self.browser.find_element_by_id('map').value_of_css_property('width')), ('400px', '400px'))

    def test_report_button(self):
        self.browser.find_element_by_class_name('generate').click()
        self.assertEquals(
            self.browser.current_url, self.live_server_url + reverse('report', args=[1])
        )

    def test_navbar_link(self):
        self.browser.find_element_by_class_name('navbar-brand').click()
        self.assertEquals(
            self.browser.current_url, self.live_server_url + reverse('dashboard')
        )

    def test_sign_out(self):
        self.browser.find_element_by_class_name('nav-link').click()
        self.assertEquals(
            self.browser.current_url, self.live_server_url + reverse('login')
        )
