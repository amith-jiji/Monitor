import time

from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse


class TestProjectLoginPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='drivers/geckodriver.exe')
        self.browser.get(self.live_server_url + reverse('report', args=[1]))

    def tearDown(self):
        self.browser.close()

    def test_report_page_css_property(self):
        self.assertEquals(self.browser.find_element_by_class_name('heading').value_of_css_property('justify-content'),
                          'space-around')

    def test_report_page_text(self):
        self.assertEquals(self.browser.find_element_by_tag_name('h1').text, 'Report')

    '''def test_report_print_button(self):
        self.browser.find_element_by_class_name('table-button').click()'''

    def test_report_table(self):
        element = [i.text for i in self.browser.find_elements_by_tag_name('th')]
        self.assertEquals(
            element, ['Date', 'Time', 'Image']
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
