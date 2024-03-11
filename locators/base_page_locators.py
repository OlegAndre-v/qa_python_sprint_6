from selenium.webdriver.common.by import By


class BasePageLocators:
    ACCEPT_COOKIES = (By.XPATH, ".//*[@id='rcc-confirm-button']")
    YANDEX = (By.XPATH, ".//*[@alt='Yandex']")
    LOGO_SCOOTER = (By.XPATH, ".//*[@alt='Scooter']")
