from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")

start = time.time()

button = driver.find_element(
    By.XPATH,
    "//button[contains(text(),'Autoclosable Success Message')]"
)
button.click()

# Fixed wait
time.sleep(3)

print("Sleep completed")

end = time.time()

print("Execution Time:", round(end - start, 2), "seconds")

driver.quit()