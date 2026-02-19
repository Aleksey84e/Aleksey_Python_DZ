import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://uitestingplayground.com/dynamicid")
driver.maximize_window()
locator_class = (By.CSS_SELECTOR, "button.btn.btn-primary")
selected_locator = locator_class
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable(selected_locator))
button.click()

time.sleep(5)
driver.quit()
