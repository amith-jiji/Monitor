import pytest
from selenium import webdriver
from django.urls import reverse


@pytest.fixture(scope="class")
def driver_init(request):
    ff_driver = webdriver.Firefox(executable_path='drivers/geckodriver.exe')
    request.cls.driver = ff_driver
    yield
    ff_driver.close()


@pytest.mark.usefixtures("driver_init")
class BaseTest:
    pass


class TestMonitoring(BaseTest):
    def test_integration(self, live_server):
        self.driver.get(live_server.url)
        assert self.driver.find_element_by_class_name('box').value_of_css_property('position') == 'absolute'
        self.driver.find_element_by_tag_name('button').click()
        assert self.driver.find_element_by_tag_name('p').text == "Invalid Credentials!!Please Check your Data"
        self.driver.find_element_by_id('Email').send_keys("Sdistancemonitoring@gmail.com")
        self.driver.find_element_by_id('Password').send_keys("Sdistance@cs8a")
        self.driver.find_element_by_tag_name('button').click()

        assert self.driver.find_element_by_tag_name('body').value_of_css_property(
            'background-color') == 'rgb(187, 186, 232)'
        self.driver.find_element_by_id('camera1-button').click()

        assert self.driver.find_element_by_class_name('box').value_of_css_property('flex-direction') == 'column'
        assert self.driver.find_element_by_id('map').value_of_css_property('height'), self.driver.find_element_by_id(
            'map').value_of_css_property('width') == ('400px', '400px')
        assert self.driver.find_element_by_class_name('stream').get_attribute('src') == 'http://127.0.0.1:8000/camera1'
        self.driver.find_element_by_class_name('generate').click()

        assert self.driver.find_element_by_class_name('heading').value_of_css_property('justify-content') == 'space-around'
        assert self.driver.find_element_by_tag_name('h1').text == 'Report'
        element = [i.text for i in self.driver.find_elements_by_tag_name('th')]
        assert element == ['Date', 'Time', 'Image']
        self.driver.find_element_by_class_name('nav-link').click()
        assert self.driver.current_url == live_server.url + reverse('login')

        print("Integration Test of Social Distancing Monitor is Successful")
        return None
