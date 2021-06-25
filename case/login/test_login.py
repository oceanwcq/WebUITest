import unittest
from parameterized import parameterized
from page.login.login_page import LoginPage
from tool.read_data import ReadData
from selenium import webdriver
import time


def get_data():
    datas = ReadData("../../data/login/login.xlsx").read_data("login_fail")
    arrays = []
    for i in range(len(datas)):
        arrays.append((datas[i][1], datas[i][2], datas[i][3], datas[i][4]))
    return  arrays

class TestLogin(unittest.TestCase):


    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(options=options)
        self.loginpage = LoginPage(self.driver, "https://192.168.41.98/")
        self.loginpage.openbrowser()

    def tearDown(self):
        self.driver.quit()

    @parameterized.expand([("1", "1")])
    def test_login(self, username, password):
        time.sleep(2)
        self.loginpage.login_user(username, password)
        time.sleep(2)
        self.assertIn("config.cgi", self.loginpage.geturl())

    @parameterized.expand(get_data())
    def test_login_invalid(self, username, password, location, alerts):
        time.sleep(2)
        self.loginpage.login_user(username, password)
        time.sleep(2)
        expectAlert = "Incorrect login information. Please check the username and password and try again."
        self.assertEqual(alerts, self.loginpage.get_alert())
        self.loginpage.comfirm_alert()
        self.assertIn(location, self.loginpage.geturl())

if __name__ == '__main__':
    unittest.main()
