from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Create Chrome browser
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

# Wait for elements up to 10 seconds
driver.implicitly_wait(10)

# Open website
driver.get("https://www.lambdatest.com/selenium-playground/")

# Print page title
print("Page Title:", driver.title)

input("Press Enter to close the browser...")

driver.quit()