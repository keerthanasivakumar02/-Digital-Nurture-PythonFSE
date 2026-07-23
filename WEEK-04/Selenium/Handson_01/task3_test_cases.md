# Task 3 - Writing Test Cases

## What is a Test Case?

A Test Case is a document that describes how to verify a specific functionality of an application.

A good test case contains:
- Test Case ID
- Test Scenario
- Preconditions
- Test Steps
- Test Data
- Expected Result
- Actual Result
- Status (Pass/Fail)

---

## Example - Login Page Test Cases

### Test Case 1

**Test Case ID:** TC_LOGIN_001

**Scenario:**
Verify login with valid credentials.

**Precondition:**
User account exists.

**Test Steps:**
1. Open the Login page.
2. Enter a valid username.
3. Enter a valid password.
4. Click the Login button.

**Test Data:**

Username: admin

Password: admin123

**Expected Result:**

The user should be redirected to the Dashboard.

**Actual Result:**

User successfully navigated to the Dashboard.

**Status:**

PASS

---

### Test Case 2

**Test Case ID:** TC_LOGIN_002

**Scenario:**
Verify login with an invalid password.

**Precondition:**
User account exists.

**Test Steps:**
1. Open the Login page.
2. Enter a valid username.
3. Enter an incorrect password.
4. Click Login.

**Test Data:**

Username: admin

Password: wrong123

**Expected Result:**

An error message "Invalid Username or Password" should be displayed.

**Actual Result:**

Error message displayed successfully.

**Status:**

PASS

---

### Test Case 3

**Test Case ID:** TC_LOGIN_003

**Scenario:**
Verify login with empty fields.

**Precondition:**
Login page is opened.

**Test Steps:**
1. Leave Username empty.
2. Leave Password empty.
3. Click Login.

**Expected Result:**

Validation messages should be displayed for mandatory fields.

**Actual Result:**

Validation messages displayed.

**Status:**

PASS