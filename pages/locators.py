from selenium.webdriver.common.by import By
from base_page import BasePage


class MainPageLocators(BasePage):
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators(BasePage):
    login_form = (By.CSS_SELECTOR, 'form[id="login_form"]')
    register_form = (By.CSS_SELECTOR, 'form[id="register_form"]')


class ProductPageLocators(BasePage):
    add_to_basket = (By.CSS_SELECTOR, 'button[value="Add to basket"]')
    book_name = (By.TAG_NAME, 'h1')
    alert_book_added = (By.CSS_SELECTOR, '.alertinner  strong')
