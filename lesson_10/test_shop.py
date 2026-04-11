import pytest
import allure
from selenium import webdriver
from pages import LoginPage, InventoryPage, CartPage, CheckoutPage


@allure.feature("Покупка товаров")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Сквозной сценарий оформления заказа")
@allure.description(
    "Тест проверяет полный цикл: авторизацию, добавление 3-х товаров в корзину и проверку финальной стоимости.")
def test_purchase_flow() -> None:
    """
    Основной тест флоу покупки.
    Returns: None
    """
    with allure.step("Запуск браузера Firefox"):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)

    try:
        with allure.step("Переход на сайт Swag Labs"):
            driver.get("https://www.saucedemo.com/")

        login_page = LoginPage(driver)
        inventory = InventoryPage(driver)
        cart = CartPage(driver)
        checkout = CheckoutPage(driver)

        login_page.login("standard_user", "secret_sauce")

        with allure.step("Выбор товаров и переход в корзину"):
            inventory.add_to_cart("Sauce Labs Backpack")
            inventory.add_to_cart("Sauce Labs Bolt T-Shirt")
            inventory.add_to_cart("Sauce Labs Onesie")
            inventory.go_to_cart()

        with allure.step("Оформление заказа в корзине"):
            cart.click_checkout()

        with allure.step("Ввод данных получателя и получение счета"):
            checkout.fill_info("Alex", "Popov", "654321")
            total_text = checkout.get_total_price()

        with allure.step("Проверка итоговой суммы"):
            with allure.step(f"Убедиться, что сумма '{total_text}' содержит '$58.29'"):
                assert "Total: $58.29" in total_text, f"Ожидалась сумма $58.29, но получили: {total_text}"

    finally:
        with allure.step("Закрытие браузера"):
            driver.quit()