from selenium import webdriver
import time


class BasePage(object):

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def openbrowser(self):
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

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(chrome_options=options)
    basepage = BasePage(driver, 'https://192.168.41.98/')
    basepage.openbrowser()
    time.sleep(2)
    basepage.closebrowser()