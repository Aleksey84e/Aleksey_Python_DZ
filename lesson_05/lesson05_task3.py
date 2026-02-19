import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get('http://the-internet.herokuapp.com/inputs')

wait = WebDriverWait(driver, 10)
input_field = wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))

input_field.send_keys("Sky")
time.sleep(2)

input_field.clear()
time.sleep(2)

input_field.send_keys("Pro")
sleep(5)

driver.quit()