from base_page import BasePage
from selenium.webdriver.common.by import By
from locators import ProductPageLocators as PPL


class ProductPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.url = url

    def should_be_submit_button(self):
        return self.is_element_present(*PPL.add_to_basket)

    @property
    def click_submit_button(self):
        return self.driver.find_element(*PPL.add_to_basket)

    @property
    def book_name(self):
        return self.driver.find_element(*PPL.book_name)

    @property
    def alert_book_added(self):
        return self.driver.find_element(*PPL.alert_book_added)
