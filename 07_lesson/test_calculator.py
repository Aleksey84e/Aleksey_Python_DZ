import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


def test_slow_calculator_result():
    # Настройка драйвера
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Инициализация страницы
    calc_page = CalculatorPage(driver)

    # Выполнение шагов
    calc_page.open()
    calc_page.set_delay("45")

    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    # Получение результата (таймаут 50 секунд для запаса)
    result = calc_page.get_result_text(50)

    # Проверка
    assert result == "15"

    # Закрытие драйвера
    driver.quit()
