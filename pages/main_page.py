from base_page import BasePage
from selenium.webdriver.common.by import By
from locators import MainPageLocators as MPL
from login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.driver.find_element(*MPL.LOGIN_LINK)
        link.click()
        return LoginPage(driver=self.driver, url=self.driver.current_url)

    def should_be_login_link(self):
        return self.is_element_present(*MPL.LOGIN_LINK), "Login link is not presented"
