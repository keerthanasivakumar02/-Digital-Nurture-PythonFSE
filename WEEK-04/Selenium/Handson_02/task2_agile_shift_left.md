# Task 2 - Agile QA and Shift-Left Testing

## Objective

Understand how QA participates in Agile development and how Shift-Left Testing helps detect defects early.

---

# 1. Problems with Waterfall Testing

In the Waterfall model, testing starts only after development is completed.

### Problem 1 - Late Defect Detection

Defects are found only after coding is finished, making them more expensive and time-consuming to fix.

### Problem 2 - Requirement Misunderstanding

If requirements are misunderstood, the issue may only be discovered during testing, leading to significant rework.

### Problem 3 - Delayed Product Delivery

Fixing multiple defects at the end of development delays the project release.

---

# 2. QA Role in Agile Ceremonies

## Sprint Planning

- Review user stories.
- Define acceptance criteria.
- Estimate testing effort.
- Clarify requirements with the team.

---

## Daily Stand-up

- Share testing progress.
- Report blockers.
- Coordinate with developers.

---

## Sprint Review

- Verify completed features.
- Demonstrate tested functionality.
- Confirm acceptance criteria are met.

---

## Sprint Retrospective

- Discuss what went well.
- Identify testing improvements.
- Suggest process changes for future sprints.

---

# 3. Shift-Left Testing Practices

## 1. Requirement Review

QA reviews requirements before development begins to identify ambiguities and ensure they are testable.

---

## 2. Write Test Cases Before Coding

QA prepares test cases early, allowing developers to understand expected behavior before implementation.

---

## 3. Static Code Analysis

Developers use tools to detect coding issues before executing the application.

Examples:
- SonarQube
- Pylint

---

## 4. API Contract Testing

Verify API request and response formats before integrating different modules.

Example:

POST /courses

Request:

{
  "courseCode": "CS101",
  "courseName": "Python"
}

Expected Response:

201 Created

---

# 4. Acceptance Criteria (Gherkin)

## Scenario 1 - Happy Path

Given the college administrator is logged in

When the administrator enters a unique course code and valid course details

Then the course should be created successfully.

---

## Scenario 2 - Duplicate Course Code

Given a course with code "CS101" already exists

When the administrator tries to create another course with the same code

Then the system should display an error message indicating that the course code already exists.

---

## Scenario 3 - Missing Required Fields

Given the administrator is on the Create Course page

When the administrator submits the form without entering mandatory fields

Then validation messages should be displayed and the course should not be created.

---

# Benefits of Shift-Left Testing

- Early defect detection.
- Reduced development cost.
- Improved software quality.
- Better collaboration between QA and developers.
- Faster delivery.