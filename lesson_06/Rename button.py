from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")

wait = WebDriverWait(driver, 10)
input_field = wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))
input_field.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
waiter = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#updatingButton"))
    )
loaded_text = waiter.text
print(loaded_text)

driver.quit()








#driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
#waiter = WebDriverWait(driver, 20).until(
#        EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
#    )
#loaded_text = waiter.text
#print(loaded_text)

#driver.quit()
