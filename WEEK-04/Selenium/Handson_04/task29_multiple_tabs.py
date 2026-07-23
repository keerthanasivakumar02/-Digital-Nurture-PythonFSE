from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Create Chrome browser
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

# Open first website
driver.get("https://www.google.com")

print("First Tab Title:", driver.title)

# Open a new tab
driver.switch_to.new_window("tab")

# Open second website in new tab
driver.get("https://www.wikipedia.org")

print("Second Tab Title:", driver.title)

# Get all window handles
tabs = driver.window_handles

# Switch back to first tab
driver.switch_to.window(tabs[0])

print("Back to First Tab:", driver.title)

input("Press Enter to close...")

driver.quit()