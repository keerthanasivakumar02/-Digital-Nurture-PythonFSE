# Hands-on 6 – Running Selenium Tests with pytest

## Objective
Learn how to execute Selenium automation scripts using pytest by implementing fixtures, assertions, parameterized tests, HTML reports, and screenshot capture on test failure.

## Topics Covered
- pytest Test Discovery
- Fixtures (conftest.py)
- Assertions
- Parameterized Tests
- HTML Test Reports
- Screenshot on Failure
- Selenium WebDriver with pytest

## Project Structure

```
Handson_06/
│── conftest.py
│── test_playground.py
│── README.md
│── report.html
```

## Requirements

Install the required packages:

```bash
pip install selenium pytest pytest-html
```

## Tests Implemented

### 1. Simple Form Submission
- Opens the Simple Form Demo page
- Enters a message
- Clicks "Get Checked Value"
- Verifies the displayed message

### 2. Checkbox Demo
- Opens Checkbox Demo
- Selects the checkbox
- Verifies it is selected
- Unchecks it
- Verifies it is deselected

### 3. Dropdown Selection
- Opens Select Dropdown List page
- Selects "Wednesday"
- Verifies the selected option

## Parameterized Test

The Simple Form Submission test is executed with three different values:

- Hello
- Selenium Automation
- 12345

## Fixtures

### driver Fixture
- Creates a Chrome browser
- Maximizes the window
- Closes the browser after each test

### base_url Fixture
```
https://www.lambdatest.com/selenium-playground/
```

Used across all tests to avoid hardcoded URLs.

## Screenshot on Failure

If any test fails, pytest automatically captures a screenshot with the test name.

Example:

```
test_simple_form_submission_failure.png
```

## Commands

Run all tests

```bash
python -m pytest test_playground.py -v
```

Run tests with console output

```bash
python -m pytest test_playground.py -v -s
```

Generate HTML report

```bash
python -m pytest test_playground.py --html=report.html --self-contained-html
```

## Expected Output

```
5 passed
```

## Outcome

Successfully implemented Selenium automation testing using pytest with:

- Fixtures
- Assertions
- Parameterized Tests
- HTML Reports
- Screenshot Capture
- Selenium WebDriver