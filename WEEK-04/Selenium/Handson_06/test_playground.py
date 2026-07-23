


# ==========================================================
# HANDS-ON 5 REFERENCE CODE (Kept for Future Use)
# ==========================================================
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# def test_simple_form_submission(driver):
#     # Open Simple Form Demo
#     driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
#
#     # Wait until input box is visible
#     wait = WebDriverWait(driver, 10)
#
#     message_box = wait.until(
#         EC.visibility_of_element_located((By.ID, "user-message"))
#     )
#
#     # Enter text
#     message_box.send_keys("Hello Selenium")
#
#     # Click Get Checked Value button
#     submit_button = driver.find_element(By.ID, "showInput")
#     submit_button.click()
#
#     # Wait until output message appears
#     output = wait.until(
#         EC.visibility_of_element_located((By.ID, "message"))
#     )
#
#     # Assertion
#     assert output.text == "Hello Selenium"
#
#
# def test_checkbox_demo(driver):
#     driver.get("https://www.lambdatest.com/selenium-playground/checkbox-demo")
#
#     wait = WebDriverWait(driver, 10)
#
#     checkbox = wait.until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='checkbox']"))
#     )
#
#     checkbox.click()
#     assert checkbox.is_selected()
#
#     checkbox.click()
#     assert not checkbox.is_selected()

# ==========================================================
# HANDS-ON 6 CODE STARTS BELOW
# ==========================================================

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@pytest.mark.parametrize("message", [
    "Hello",
    "Selenium Automation",
    "12345"
])
def test_simple_form_submission(driver, base_url, message):

    driver.get(base_url + "simple-form-demo")

    wait = WebDriverWait(driver, 20)

    message_box = wait.until(
        EC.presence_of_element_located((By.ID, "user-message"))
    )

    message_box.clear()
    message_box.send_keys(message)

    driver.find_element(By.ID, "showInput").click()

    # Wait until the message is actually displayed
    wait.until(lambda d: d.find_element(By.ID, "message").text != "")

    output = driver.find_element(By.ID, "message")

    print("Expected:", message)
    print("Actual  :", output.text)

    assert output.text == message

def test_checkbox_demo(driver, base_url):

    driver.get(base_url + "checkbox-demo")

    wait = WebDriverWait(driver, 10)

    checkbox = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='checkbox']"))
    )

    checkbox.click()
    assert checkbox.is_selected()

    checkbox.click()
    assert not checkbox.is_selected()

from selenium.webdriver.support.ui import Select

def test_dropdown_selection(driver, base_url):

    driver.get(base_url + "select-dropdown-demo")

    wait = WebDriverWait(driver, 10)

    dropdown = wait.until(
        EC.presence_of_element_located((By.ID, "select-demo"))
    )

    select = Select(dropdown)
    select.select_by_visible_text("Wednesday")

    assert select.first_selected_option.text == "Wednesday"
#test fails 
#def test_page_title(driver, base_url):
#    driver.get(base_url + "simple-form-demo")
#    assert "Selenium Playground" in driver.title