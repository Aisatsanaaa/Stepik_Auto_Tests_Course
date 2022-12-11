from time import sleep
import pytest
from selenium.webdriver.common.by import By
from login_page import LoginPage
from main_page import MainPage

LINK = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_see_login_url(driver):
    page = MainPage(driver, LINK)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()
    assert 'login' in driver.current_url, "Login url is not presented"


def test_guest_can_see_login_form(driver):
    page = MainPage(driver, LINK)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()
    login_page.should_be_login_form()


def test_guest_can_see_register_form(driver):
    page = MainPage(driver, LINK)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()
    login_page.should_be_register_form()

