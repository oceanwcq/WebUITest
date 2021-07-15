import unittest
from parameterized import parameterized
from page.login.login_page import LoginPage
from page.device_configuration_page import DeviceConfiguration
from selenium import webdriver
import time

def get_device_name_data():
    pass

class TestDevicePage(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(options=options)
        self.loginpage = LoginPage(self.driver, "https://192.168.41.98/")
        self.loginpage.openbrowser()
        self.loginpage.login_user('1', '1')
        self.devicepage = DeviceConfiguration(self.driver, "https://192.168.41.98/")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    @parameterized.expand([("test1"), ("Sz!12345")])
    def test_device_name(self, devicename):
        self.devicepage.input_device_name(devicename);
        self.devicepage.click_apply()
        self.devicepage.comfirm_alert();
        self.assertEqual(devicename, self.devicepage.get_device_name())