import pytest
import allure
from selenium import webdriver
from calculator_page import CalculatorPage


@allure.feature("Функциональность калькулятора")
@allure.story("Операции с задержкой")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка сложения в медленном калькуляторе")
@allure.description("Тест проверяет, что сумма 7 + 8 корректно отображается после задержки в 45 секунд.")
def test_slow_calculator_result() -> None:
    """
    Тест инициализирует браузер, выполняет сложение чисел на странице
    медленного калькулятора и проверяет итоговое значение.
    """

    with allure.step("Запуск браузера Chrome"):
        driver = webdriver.Chrome()
        driver.maximize_window()

    calc_page = CalculatorPage(driver)

    with allure.step("Открытие страницы и установка задержки"):
        calc_page.open()
        calc_page.set_delay("45")

    with allure.step("Ввод математического выражения: 7 + 8 ="):
        calc_page.click_button("7")
        calc_page.click_button("+")
        calc_page.click_button("8")
        calc_page.click_button("=")

    with allure.step("Ожидание и получение результата"):

        result = calc_page.get_result_text(50)

    with allure.step("Проверка итогового значения"):
        with allure.step(f"Убедиться, что полученный результат '{result}' равен '15'"):
            assert result == "15", f"Ошибка: ожидалось 15, но получили {result}"

    with allure.step("Закрытие браузера"):
        driver.quit()