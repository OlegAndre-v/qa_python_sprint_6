import allure
import pytest

from data import *
from locators.main_page_locators import *


@allure.story('Тесты выпадающего списка "Вопросы о важном"')
class TestDropDownList:
    @allure.title('Тест соответсвия текста ответа')
    @pytest.mark.parametrize('question, answer, td_answer', [
        [MainPageLocators.QUESTION_1, MainPageLocators.ANSWER_1, TDAnswer.ANSWER1],
        [MainPageLocators.QUESTION_2, MainPageLocators.ANSWER_2, TDAnswer.ANSWER2],
        [MainPageLocators.QUESTION_3, MainPageLocators.ANSWER_3, TDAnswer.ANSWER3],
        [MainPageLocators.QUESTION_4, MainPageLocators.ANSWER_4, TDAnswer.ANSWER4],
        [MainPageLocators.QUESTION_5, MainPageLocators.ANSWER_5, TDAnswer.ANSWER5],
        [MainPageLocators.QUESTION_6, MainPageLocators.ANSWER_6, TDAnswer.ANSWER6],
        [MainPageLocators.QUESTION_7, MainPageLocators.ANSWER_7, TDAnswer.ANSWER7],
        [MainPageLocators.QUESTION_8, MainPageLocators.ANSWER_8, TDAnswer.ANSWER8]
    ])
    def test_drop_down_text(self, driver, main_page, question, answer, td_answer):
        main_page.open()
        main_page.accept_cookies()
        assert main_page.get_text_from_drop_down_list(question, answer) == td_answer
