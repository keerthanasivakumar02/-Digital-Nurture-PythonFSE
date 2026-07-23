from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

# Create Chrome browser
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

# Open website
driver.get("https://www.lambdatest.com/selenium-playground/")

# Screenshot file name
file_name = "homepage.png"

# Capture screenshot
driver.save_screenshot(file_name)

# Check whether screenshot is saved
if os.path.exists(file_name):
    print("Screenshot saved successfully.")
else:
    print("Screenshot not saved.")

input("Press Enter to close the browser...")

driver.quit()