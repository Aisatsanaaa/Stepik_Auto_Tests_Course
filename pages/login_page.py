from base_page import BasePage
from selenium.webdriver.common.by import By
from locators import MainPageLocators as MPL
from locators import LoginPageLocators as LPL


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        return self.driver.find_element(*MPL.LOGIN_LINK)

    def should_be_login_form(self):
        return self.driver.find_element(*LPL.login_form)

    def should_be_register_form(self):
        return self.driver.find_element(*LPL.register_form)
