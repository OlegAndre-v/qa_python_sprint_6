import allure
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Метод получения текста из выпадающего списка')
    def get_text_from_drop_down_list(self, question_locator, answer_locator):
        self.click_element(question_locator)
        return self.get_text(answer_locator)
