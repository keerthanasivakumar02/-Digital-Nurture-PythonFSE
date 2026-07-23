from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Create Chrome browser
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

# Open first website
driver.get("https://www.google.com")
print("Opened:", driver.title)

# Open second website
driver.get("https://www.wikipedia.org")
print("Opened:", driver.title)

# Go back
driver.back()
print("After Back:", driver.title)

# Go forward
driver.forward()
print("After Forward:", driver.title)

# Refresh the page
driver.refresh()
print("Page Refreshed")

# Print current URL
print("Current URL:", driver.current_url)

input("Press Enter to close the browser...")

driver.quit()