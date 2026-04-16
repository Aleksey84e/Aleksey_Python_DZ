import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Класс страницы 'Slow Calculator' для реализации паттерна Page Object.
    Содержит локаторы и методы взаимодействия с элементами калькулятора.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует драйвер и основные локаторы страницы.

        Args:
            driver (WebDriver): Экземпляр Selenium WebDriver.

        Returns:
            None
        """
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"


        self._delay_input = (By.CSS_SELECTOR, "#delay")
        self._result_field = (By.CLASS_NAME, "screen")
        self._button_template = "//span[text()='{0}']"

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """
        Выполняет переход по URL адресу калькулятора.

        Returns:
            None
        """
        self.driver.get(self.url)

    @allure.step("Установить задержку вычислений: {seconds} сек.")
    def set_delay(self, seconds: str) -> None:
        """
        Очищает поле ввода задержки и вводит новое значение.

        Args:
            seconds (str): Время задержки в секундах.

        Returns:
            None
        """
        delay = self.driver.find_element(*self._delay_input)
        delay.clear()
        delay.send_keys(seconds)

    @allure.step("Нажать на кнопку '{value}'")
    def click_button(self, value: str) -> None:
        """
        Находит кнопку по тексту (цифру или оператор) и кликает по ней.

        Args:
            value (str): Текстовое значение кнопки (например, '7', '+', '=').

        Returns:
            None
        """
        xpath = self._button_template.format(value)
        self.driver.find_element(By.XPATH, xpath).click()

    @allure.step("Получить текст результата с ожиданием {timeout} сек.")
    def get_result_text(self, timeout: int) -> str:
        """
        Ожидает появления конкретного результата (15) и возвращает текст из поля.

        Args:
            timeout (int): Время ожидания появления текста в секундах.

        Returns:
            str: Текст, отображаемый на экране калькулятора.
        """
        wait = WebDriverWait(self.driver, timeout)

        wait.until(EC.text_to_be_present_in_element(self._result_field, "15"))
        return self.driver.find_element(*self._result_field).text