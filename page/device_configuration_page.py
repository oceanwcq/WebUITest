
from selenium import webdriver
from base.basepage import BasePage
from page.login.login_page import LoginPage
from selenium.webdriver.common.by import By
import time

class DeviceConfiguration(BasePage):

    # Element locators
    device_name_locator = (By.NAME, "cfg_device_name")
    apply_button_locator = (By.ID, "save_1")

    def get_device_name(self):
        return self.get_value(self.device_name_locator)

    def input_device_name(self, text):
        return self.input_text(self.device_name_locator, text)

    def click_apply(self):
        self.click_element(self.apply_button_locator)


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)
    loginpage = LoginPage(driver, "https://192.168.41.98/")
    loginpage.openbrowser()
    loginpage.login_user("1", "1")
    devicePage = DeviceConfiguration(driver, "https://192.168.41.98/")
    devicePage.input_device_name('温暖的超群')
    devicePage.click_apply()
    devicePage.comfirm_alert()
    time.sleep(1)
    print(devicePage.get_device_name())
