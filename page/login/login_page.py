from selenium import webdriver
import time
from base.basepage import BasePage

class LoginPage(BasePage):

    def enter_username(self, text):
        self.driver.find_element_by_id("name").send_keys(text)

    def enter_password(self, text):
        self.driver.find_element_by_id("passwd").send_keys(text)

    def click_login(self):
        self.driver.find_element_by_id("login").click()

    def login_user(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(chrome_options=options)
    loginpage = LoginPage(driver, 'https://192.168.41.98/')
    loginpage.openbrowser()
    time.sleep(2)
    loginpage.enter_username('1')
    loginpage.enter_password("1")
    loginpage.click_login()