from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Create Chrome browser
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

# Open website
driver.get("https://www.lambdatest.com/selenium-playground/")

# Get current window size
size = driver.get_window_size()
print("Current Window Size:", size)

# Set new window size
driver.set_window_size(1200, 800)

# Get updated window size
new_size = driver.get_window_size()
print("Updated Window Size:", new_size)

input("Press Enter to close the browser...")

driver.quit()