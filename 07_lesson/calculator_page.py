from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

        # Локаторы
        self._delay_input = (By.CSS_SELECTOR, "#delay")
        self._result_field = (By.CLASS_NAME, "screen")
        # Универсальный локатор для кнопок по тексту
        self._button_template = "//span[text()='{0}']"

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds):
        delay = self.driver.find_element(*self._delay_input)
        delay.clear()
        delay.send_keys(seconds)

    def click_button(self, value):
        xpath = self._button_template.format(value)
        self.driver.find_element(By.XPATH, xpath).click()

    def get_result_text(self, timeout):
        # Ожидаем, пока текст "15" появится в поле результата
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.text_to_be_present_in_element(self._result_field, "15"))
        return self.driver.find_element(*self._result_field).text
