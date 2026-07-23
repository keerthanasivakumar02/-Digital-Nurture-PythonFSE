from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")

wait = WebDriverWait(driver, 10)

# Click the button
button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'Autoclosable Success Message')]")
    )
)
button.click()

# Wait until the alert contains some text
alert = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//div[contains(@class,'alert-success')]")
    )
)

wait.until(lambda d: alert.text.strip() != "")

print("Alert Text:", alert.text)

driver.quit()