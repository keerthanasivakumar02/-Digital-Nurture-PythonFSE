# Hands-on 7 – Page Object Model (POM) with Selenium and Pytest

## Objective

The objective of this hands-on is to implement the **Page Object Model (POM)** design pattern using Selenium WebDriver and Pytest. The project automates multiple Selenium Playground scenarios using reusable Page Object classes and executes them as a single test suite.

---

## Technologies Used

- Python 3.12
- Selenium WebDriver
- Pytest
- Chrome Browser
- ChromeDriver
- pytest-html

---

## Test Scenarios

The test suite includes the following scenarios:

- Simple Form Demo
- Checkbox Demo
- Select Dropdown Demo
- Input Form Demo

Each scenario is implemented using the **Page Object Model (POM)** to improve code readability, reusability, and maintainability.

---

## Run the Test Suite

Execute all test scenarios using:

```bash
python -m pytest tests/test_playground.py -v --html=report.html --self-contained-html
```

---

## HTML Report

After execution, an HTML report named **report.html** is generated in the project directory.

Open the report in any web browser to view:

- Test execution summary
- Passed and failed test cases
- Execution time
- Detailed test results

---

## Advantages of Page Object Model (POM)

- Separates page locators from test logic.
- Improves code readability.
- Encourages code reuse.
- Simplifies maintenance.
- Reduces duplicate code.
- Makes the automation framework scalable.

---

## POM Maintenance Benefit

In a traditional Selenium script, if the **Submit** button ID changes from **`submit`** to **`btn-submit`**, every test script containing that locator must be updated.

With the **Page Object Model (POM)**, the locator is stored only once in the corresponding Page Object class. Updating the locator in that single class automatically updates all tests that use it, making maintenance faster and easier.

---

## Outcome

- Implemented the Page Object Model (POM) framework.
- Automated Selenium Playground test scenarios.
- Executed all scenarios through a single Pytest test suite.
- Generated a self-contained HTML execution report.