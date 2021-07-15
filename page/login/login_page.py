from selenium import webdriver
import time
from base.basepage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    # Element locators
    username_locator = (By.ID, "name")
    password_locator = (By.ID, "passwd")
    login_locator = (By.ID, "login")

    # Actions
    def enter_username(self, text):
        # self.driver.find_element_by_id("name").send_keys(text)
        self.input_text(self.username_locator, text)

    def enter_password(self, text):
        # self.driver.find_element_by_id("passwd").send_keys(text)
        self.input_text(self.password_locator, text)

    def click_login(self):
        # self.driver.find_element_by_id("login").click()
        self.click_element(self.login_locator)

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