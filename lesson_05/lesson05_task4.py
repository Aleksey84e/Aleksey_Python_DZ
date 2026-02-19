import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()
driver.get('http://the-internet.herokuapp.com/login')

wait = WebDriverWait(driver, 5)
search_input = driver.find_element(By.CSS_SELECTOR, "input#username")
search_input.send_keys("tomsmith")
time.sleep(5)

wait = WebDriverWait(driver, 5)
search_input = driver.find_element(By.CSS_SELECTOR, "input#password")
search_input.send_keys("SuperSecretPassword")
time.sleep(5)

locator_class = (By.CSS_SELECTOR, "button.radius")
selected_locator = locator_class
wait = WebDriverWait(driver, 5)
button = wait.until(EC.element_to_be_clickable(selected_locator))
button.click()

time.sleep(5)
driver.quit()