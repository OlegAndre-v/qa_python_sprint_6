# Проект по UI тестированию https://qa-scooter.praktikum-services.ru/
## Структура проекта
 - allure_results/ - Директория с отчетами о тестировании. Команда для просмотра отчета ```allure serve allure_results```, для формирования отчета ```pytest tests --alluredir=allure_results```

 - locators/ - Директория с локаторами
 - pages/ - Директория с методами
    - base_page
        - open - Метод открытия браузера на заданном urle.
        - get_url - Метод сбора текущего urla.
        - click_element - Метод ожидания и клика по элементу.
        - send_input - Метод ожидания и отправки данных элементу.
        - get_text - Метод сбора текста в элементе.
        - accept_cookies - Метод принятия куков.
        - tab_switch - Метод переключения таба браузера, на вновь открытый.
    - main_page
        - get_text_from_drop_down_list - Метод получения текста из выпадающего списка.
    - order_page
        - fill_order_form_for_whom - Метод заполнения формы "Для кого самокат".
        - fill_order_form_about_rent - Метод заполнения формы "Про аренду".
        - order_issued_check - Метод проверки успешного оформления заказа.
 -tests/
    - test_drop_down_list - Модуль тестов выпадающего списка.
      - test_drop_down_text - Тест соответствия текста ответа.
    - test_logo_transition - Модуль тестов переходов по логотипу.
      - test_logo_scooter - Тест перехода по логотипу самоката.
      - test_logo_yandex - Тест перехода по логотиау яндекса.
    - test_scooter_order - Модуль тестов оформления заказа.
      - test_scooter_order - Позитивный тест заказа самокатов.
 - conftest - Модуль фикстур проекта.
 - data - Модуль с ТД проекта.
 - requirements - Модуль с внешними зависимостями для установки ```pip install -r requirements.txt```
      
