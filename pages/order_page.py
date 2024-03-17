import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step('Заполнение формы "Для кого самокат"')
    def fill_order_form_for_whom(self, data):
        self.send_input(OrderPageLocators.NAME_INPUT, data.NAME)
        self.send_input(OrderPageLocators.SURNAME_INPUT, data.SURNAME)
        self.send_input(OrderPageLocators.ADDRESS_INPUT, data.ADDRESS)
        self.send_input(OrderPageLocators.UNDERGROUND_INPUT, data.UNDERGROUND)
        self.click_element(OrderPageLocators.SELECT_UNDERGROUND)
        self.send_input(OrderPageLocators.PHONE_NUMBER_INPUT, data.NUMBER)
        self.click_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Заполнение формы "Про аренду"')
    def fill_order_form_about_rent(self, data):
        self.send_input(OrderPageLocators.DATE_INPUT, data.DATE)
        self.click_element(OrderPageLocators.SELECT_COLOR_GREY)
        self.click_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_element(OrderPageLocators.RENTAL_PERIOD_ONE_DAY)
        self.send_input(OrderPageLocators.COMMENT_INPUT, data.COMMENT)
        self.click_element(OrderPageLocators.BUTTON_ORDER)

    @allure.step('Проверка успешного оформления заказа')
    def order_issued_check(self):
        return self.get_text(OrderPageLocators.ORDER_STATUS)
