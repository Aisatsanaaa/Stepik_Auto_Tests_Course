from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)
