from pages.base_page import *
from constance import *


class TestQ:
    def test_accept_cook(self, driver):
        base_page = BasePage(driver)
        base_page.open_url(Url.MAIN_PAGE)
        base_page.accept_cookies()
