import allure

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators
from data import Url


class BasePage:
    def __init__(self, driver, url_path):
        self.driver = driver
        url = Url.BASE_PAGE
        self.url = url + url_path

    @allure.step('Открытие браузера на заданной url')
    def open(self):
        url = self.url
        return self.driver.get(url)

    @allure.step('Сбор текущего "URL"')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Ожидание и клик по элементу')
    def click_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator)).click()

    @allure.step('Ожидание элимента и ввод данных')
    def send_input(self, locator, data, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator)).send_keys(data)

    @allure.step('Принятие куков')
    def accept_cookies(self):
        return self.click_element(BasePageLocators.ACCEPT_COOKIES)

    @allure.step('Ожидание и сбор текста элемента')
    def get_text(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator)).text

    @allure.step('Переключение на открытый при переходе таб')
    def tab_switch(self, locator, time=10):
        self.driver.switch_to.window(self.driver.window_handles[1])
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator))
