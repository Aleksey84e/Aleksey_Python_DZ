from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#award"))
    )

all_images = driver.find_elements(By.TAG_NAME, "img")

if len(all_images) >= 3:

    third_image = all_images[2]
    src_value = third_image.get_attribute("src")

    print("Значение атрибута src у 3-й картинки:")
    print(src_value)


driver.quit()