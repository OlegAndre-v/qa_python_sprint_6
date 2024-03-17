import allure

from pages.base_page import *
from data import *
from locators.external_locators import DzenLocators


@allure.story('Тесты переходов по логотипу Яндекс Самокат')
class TestLogoTransition:
    @allure.title('Тест перехода со страницы заказа на главую по клику на логотип "Самокат"')
    def test_logo_scooter(self, driver, order_page):
        order_page.open()
        order_page.click_element(BasePageLocators.LOGO_SCOOTER)
        assert order_page.get_url() == Url.MAIN_PAGE

    @allure.title('Тест перехода с главной на страницу Яндекса по клику на логотиа "Яндекс"')
    def test_logo_yandex(self, driver, main_page):
        main_page.open()
        main_page.click_element(BasePageLocators.LOGO_YANDEX)
        main_page.tab_switch(DzenLocators.SEARCH_INPUT)
        assert Url.DZEN_PAGE in main_page.get_url()
