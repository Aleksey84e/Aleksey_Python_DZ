import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://uitestingplayground.com/classattr")
button_xpath = "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]"
wait = WebDriverWait(driver, 10)
blue_button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
blue_button.click()

time.sleep(5)
driver.quit()