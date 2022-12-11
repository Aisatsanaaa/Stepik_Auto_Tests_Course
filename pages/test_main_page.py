import pytest
from selenium.webdriver.common.by import By
from main_page import MainPage
from login_page import LoginPage

LINK = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(driver):
    page = MainPage(driver, LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(driver):
    page = MainPage(driver, LINK)
    page.open()
    assert page.should_be_login_link()

