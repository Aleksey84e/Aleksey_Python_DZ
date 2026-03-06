import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
driver_path= "edge/msedgedriver.exe"
service = EdgeService(driver_path)
driver = webdriver.Edge(service=service)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_field_color(self, driver, field_id):
        field = driver.find_element(By.ID, field_id)
        return field.value_of_css_property("background-color")

def test_form_validation_colors(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.wait = WebDriverWait(driver, 10)

        try:
            self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

            self.driver.find_element(By.NAME, "first-name").send_keys("Иван")
            self.driver.find_element(By.NAME, "last-name").send_keys("Петров")
            self.driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
            self.driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
            self.driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
            self.driver.find_element(By.NAME, "zip-code").clear()
            self.driver.find_element(By.NAME, "city").send_keys("Москва")
            self.driver.find_element(By.NAME, "country").send_keys("Россия")
            self.driver.find_element(By.NAME, "job-position").send_keys("QA")
            self.driver.find_element(By.NAME, "company").send_keys("SkyPro")
            self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-success")))

            assert "alert-danger" in driver.find_element(By.ID, "zip-code").get_attribute("class")

            fields = [
                "first-name", "last-name", "address", "city",
                "country", "e-mail", "phone", "job-position", "company"
            ]

            for field_id in fields:
                assert "alert-success" in driver.find_element(By.ID, field_id).get_attribute("class")

        finally:
           driver.quit()

if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])