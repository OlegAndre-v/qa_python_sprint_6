import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Url


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def main_page(driver):
    url_path = ''
    return MainPage(driver, url_path)


@pytest.fixture(scope='function')
def order_page(driver):
    url_path = Url.ORDER_PATH
    return OrderPage(driver, url_path)
