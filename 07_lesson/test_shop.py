import pytest
from selenium import webdriver
from pages import LoginPage, InventoryPage, CartPage, CheckoutPage


def test_purchase_flow():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)

    try:
        driver.get("https://www.saucedemo.com/")
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_to_cart("Sauce Labs Backpack")
        inventory.add_to_cart("Sauce Labs Bolt T-Shirt")
        inventory.add_to_cart("Sauce Labs Onesie")

        inventory.go_to_cart()
        cart = CartPage(driver)
        cart.click_checkout()

        checkout = CheckoutPage(driver)
        checkout.fill_info("Alex", "Popov", "654321")
        total_text = checkout.get_total_price()
        assert "Total: $58.29" in total_text

    finally:
        driver.quit()
