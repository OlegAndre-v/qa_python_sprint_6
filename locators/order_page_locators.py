from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class OrderPageLocators(BasePageLocators):
    NAME_INPUT = (By.XPATH, ".//*[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, ".//*[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, ".//*[@placeholder='* Адрес: куда привезти заказ']")
    UNDERGROUND_INPUT = (By.XPATH, ".//*[@placeholder='* Станция метро']")
    SELECT_UNDERGROUND = (By.XPATH, ".//*[@class='select-search__row']")
    PHONE_NUMBER_INPUT = (By.XPATH, ".//*[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, ".//*[text()='Далее']")
    DATE_INPUT = (By.XPATH, ".//*[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, ".//*[text()='* Срок аренды']")
    RENTAL_PERIOD_ONE_DAY = (By.XPATH, ".//*[text()='сутки']")
    SELECT_COLOR_GREY = (By.XPATH, ".//*[@id='grey']")
    COMMENT_INPUT = (By.XPATH, ".//*[@placeholder='Комментарий для курьера']")
    BUTTON_ORDER = (By.XPATH, ".//*[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    BUTTON_YES = (By.XPATH, ".//*[text()='Да']")
    ORDER_STATUS = (By.XPATH, ".//*[text()='Посмотреть статус']")
