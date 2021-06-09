from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse


class TestProjectLoginPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='drivers/geckodriver.exe')
        self.browser.get(self.live_server_url)

    def tearDown(self):
        self.browser.close()

    def test_login_page_css_property(self):
        self.assertEquals(self.browser.find_element_by_class_name('box').value_of_css_property('position'), 'absolute')

    def test_submit_button_invalid_login(self):
        self.browser.find_element_by_tag_name('button').click()
        self.assertEquals(
            self.browser.find_element_by_tag_name('p').text, "Invalid Credentials!!Please Check your Data"
        )

    def test_submit_button_valid_login(self):
        add_url = self.live_server_url + reverse('dashboard')
        self.browser.find_element_by_id('Email').send_keys("Sdistancemonitoring@gmail.com")
        self.browser.find_element_by_id('Password').send_keys("Sdistance@cs8a")
        self.browser.find_element_by_tag_name('button').click()
        self.assertEquals(
            self.browser.current_url, add_url
        )
