from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        return self.driver.get(url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator))

    def click_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator)).click()

    def accept_cookies(self):
        return self.click_element(BasePageLocators.ACCEPT_COOKIES)
