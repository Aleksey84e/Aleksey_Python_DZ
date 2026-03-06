import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


def test_saucedemo_checkout():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
        wait.until(EC.visibility_of_element_located((By.ID, "login-button"))).click()
        wait = WebDriverWait(driver, 50)

        items = ["add-to-cart-sauce-labs-backpack",
                 "add-to-cart-sauce-labs-bolt-t-shirt",
                 "add-to-cart-sauce-labs-onesie"]

        for item_id in items:
            driver.find_element(By.ID, item_id).click()

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()
        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        driver.find_element(By.ID, "continue").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
        total_text = driver.find_element(By.CLASS_NAME, "summary_total_label").text
        total_value = float(total_text.replace("Total: $", ""))

        expected_total = 58.29
        assert total_value == expected_total, f"Ожидалось {expected_total}, получено {total_value}"

        print(f"✓ Тест пройден! Итоговая сумма: {total_text}")

    finally:
        driver.quit()

    if __name__ == "__main__":
        pytest.main(["-v", "-s", __file__])