from selenium import webdriver
import time


class BasePage(object):

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def openbrowser(self):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.url)

    def closebrowser(self):
        self.driver.quit()

    def geturl(self):
        return self.driver.current_url

    def comfirm_alert(self):
        self.driver.switch_to.alert.accept()

    def get_alert(self):
        return self.driver.switch_to.alert.text

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def clear_input(self, locator):
        self.find_element(locator).clear()

    def input_text(self, locator, text):
        self.clear_input(locator)
        self.find_element(locator).send_keys(text)

    def click_element(self, locator):
        self.find_element(locator).click()

    def get_value(self, locator):
        return self.find_element(locator).get_attribute("value")

if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(chrome_options=options)
    basepage = BasePage(driver, 'https://192.168.41.98/')
    basepage.openbrowser()
    time.sleep(2)
    basepage.closebrowser()