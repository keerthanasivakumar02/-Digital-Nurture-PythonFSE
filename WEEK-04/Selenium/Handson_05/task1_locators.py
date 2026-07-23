from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch Chrome
driver = webdriver.Chrome()

# Maximize browser
driver.maximize_window()

# Open LambdaTest Playground
driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

# -------------------------
# ID Locator
# -------------------------
element = driver.find_element(By.ID, "user-message")
print("ID Locator :", element.get_attribute("id"))

# -------------------------
# Name Locator
# -------------------------
element = driver.find_element(By.NAME, "message")
print("Name Locator :", element.get_attribute("name"))

# -------------------------
# Class Name Locator
# -------------------------
element = driver.find_element(By.CLASS_NAME, "form-control")
print("Class Name Locator Successful")

# -------------------------
# Tag Name Locator
# -------------------------
element = driver.find_element(By.TAG_NAME, "input")
print("Tag Name Locator Successful")

# -------------------------
# Relative XPath
# -------------------------
element = driver.find_element(
    By.XPATH,
    "//input[@id='user-message']"
)
print("Relative XPath Successful")

# -------------------------
# CSS by ID
# -------------------------
element = driver.find_element(
    By.CSS_SELECTOR,
    "#user-message"
)
print("CSS by ID Successful")

driver.quit()
"""
Preferred Locator Order

1. ID
2. CSS Selector
3. Name
4. Relative XPath
5. Class Name
6. Tag Name

Absolute XPath is avoided because it breaks whenever the page structure changes.
"""     