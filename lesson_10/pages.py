import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Класс страницы авторизации."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Args:
            driver (WebDriver): Экземпляр Selenium WebDriver.
        """
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    @allure.step("Авторизоваться пользователем {username}")
    def login(self, username: str, password: str) -> None:
        """
        Вводит учетные данные и нажимает кнопку входа.

        Args:
            username (str): Имя пользователя.
            password (str): Пароль.

        Returns:
            None
        """
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()


class InventoryPage:
    """Класс страницы каталога товаров."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Args:
            driver (WebDriver): Экземпляр Selenium WebDriver.
        """
        self.driver = driver
        self.items = {
            "Sauce Labs Backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
            "Sauce Labs Bolt T-Shirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
            "Sauce Labs Onesie": (By.ID, "add-to-cart-sauce-labs-onesie")
        }
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Добавить товар '{item_name}' в корзину")
    def add_to_cart(self, item_name: str) -> None:
        """
        Находит товар по названию в словаре и нажимает кнопку добавления.

        Args:
            item_name (str): Точное название товара из доступных в self.items.

        Returns:
            None
        """
        self.driver.find_element(*self.items[item_name]).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """
        Нажимает на иконку корзины.

        Returns:
            None
        """
        self.driver.find_element(*self.cart_link).click()


class CartPage:
    """Класс страницы корзины."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Args:
            driver (WebDriver): Экземпляр Selenium WebDriver.
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    @allure.step("Нажать кнопку 'Checkout'")
    def click_checkout(self) -> None:
        """
        Выполняет переход к оформлению заказа.

        Returns:
            None
        """
        self.driver.find_element(*self.checkout_button).click()


class CheckoutPage:
    """Класс страницы оформления заказа и проверки итогов."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Args:
            driver (WebDriver): Экземпляр Selenium WebDriver.
        """
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.zip_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполнить данные покупателя: {first} {last}")
    def fill_info(self, first: str, last: str, zip_idx: str) -> None:
        """
        Вводит персональные данные в форму оформления.

        Args:
            first (str): Имя.
            last (str): Фамилия.
            zip_idx (str): Почтовый индекс.

        Returns:
            None
        """
        self.driver.find_element(*self.first_name).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.zip_code).send_keys(zip_idx)
        self.driver.find_element(*self.continue_button).click()

    @allure.step("Получить итоговую стоимость")
    def get_total_price(self) -> str:
        """
        Считывает текст итоговой цены с экрана.

        Returns:
            str: Строка вида 'Total: $XX.XX'.
        """
        return self.driver.find_element(*self.total_label).text