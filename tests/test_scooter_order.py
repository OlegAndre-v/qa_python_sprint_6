import allure
import pytest

from data import *
from locators.order_page_locators import *


@allure.story('Тесты заказа самоката')
class TestScooterOrder:
    @allure.title('Позитивный тест заказа самоката')
    @pytest.mark.parametrize('button, data', [(OrderPageLocators.ORDER_BUTTON_UP, TDUser1),
                                              (OrderPageLocators.ORDER_BUTTON_DOWN, TDUser2)])
    def test_scooter_order(self, driver, button, data, order_page, main_page):
        main_page.open()
        order_page.accept_cookies()
        order_page.click_element(button)
        order_page.fill_order_form_for_whom(data)
        order_page.fill_order_form_about_rent(data)
        order_page.click_element(OrderPageLocators.BUTTON_YES)
        assert order_page.order_issued_check() == 'Посмотреть статус'
