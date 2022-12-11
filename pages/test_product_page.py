import time
import pytest
from time import sleep
from selenium.common.exceptions import NoAlertPresentException
import math
from product_page import ProductPage
from locators import ProductPageLocators as PPl
from selenium.webdriver.common.alert import Alert


@pytest.mark.parametrize('promo_code',
                         [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='Wrong book name')) for i in range(9)])
def test_guest_can_add_product_to_basket(driver, promo_code):
    product_url = ('http://selenium1py.pythonanywhere.com/catalogue/'
                   'coders-at-work_207/?promo=offer{}'.format(promo_code))
    product_page = ProductPage(driver, product_url)
    product_page.open()
    book = product_page.book_name.text
    product_page.should_be_submit_button()
    product_page.click_submit_button.click()
    product_page.solve_quiz_and_get_code()
    book_added = product_page.alert_book_added.text
    assert book == book_added

