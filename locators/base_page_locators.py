from selenium.webdriver.common.by import By


class BasePageLocators:
    ACCEPT_COOKIES = (By.XPATH, ".//*[@id='rcc-confirm-button']")
    LOGO_YANDEX = (By.XPATH, ".//*[@alt='Yandex']")
    LOGO_SCOOTER = (By.XPATH, ".//*[@alt='Scooter']")
    ORDER_BUTTON_UP = (By.XPATH, ".//*[@class='Button_Button__ra12g']")
    ORDER_BUTTON_DOWN = (By.XPATH, ".//*[@class='Home_FinishButton__1_cWm']")
