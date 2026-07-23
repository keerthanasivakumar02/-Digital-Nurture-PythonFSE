# ==========================================================
# HANDS-ON 5 REFERENCE CODE (Basic pytest Fixture)
# Kept for Future Use
# ==========================================================

# import pytest
# from selenium import webdriver
#
#
# @pytest.fixture(scope="function")
# def driver():
#     # Setup
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#
#     # Provide driver to the test
#     yield driver
#
#     # Teardown
#     driver.quit()

# ==========================================================
# HANDS-ON 6 CODE STARTS BELOW
# ==========================================================

import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def base_url():
    return "https://www.lambdatest.com/selenium-playground/"


@pytest.fixture(scope="function")
def driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    request.node.driver = driver

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)

        if driver:
            screenshot_name = f"{item.name}_failure.png"
            driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved: {screenshot_name}")