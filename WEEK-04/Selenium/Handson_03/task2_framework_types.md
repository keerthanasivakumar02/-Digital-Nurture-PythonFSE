# Task 2 - Compare Automation Framework Types

## Objective

Understand the different automation framework types, compare their advantages and disadvantages, recommend the best framework for a real-world project, and design a Hybrid framework folder structure.

---

# 1. Automation Framework Types

## 1. Linear Framework

### Description

The Linear Framework is the simplest automation framework where test cases are executed in a fixed sequence. Test scripts are written from start to finish without code reuse.

### Advantage

- Easy to learn and implement.

### Disadvantage

- Difficult to maintain as the project grows.

### Course Management Example

Suitable for a small project with only a few test cases such as Login and Logout.

---

## 2. Modular Framework

### Description

The application is divided into modules, and separate scripts are created for each module. These modules can be reused across different test cases.

### Advantage

- High code reusability.

### Disadvantage

- Initial framework setup takes time.

### Course Management Example

Create separate modules for:

- Login
- Course Management
- Student Management
- Logout

---

## 3. Data-Driven Framework

### Description

Test data is stored separately in files such as Excel, CSV, or JSON. The same test script executes multiple times using different data.

### Advantage

- Supports testing with multiple datasets.

### Disadvantage

- Managing test data can become complex.

### Course Management Example

Test Login with 50 different username and password combinations.

---

## 4. Keyword-Driven Framework

### Description

Test execution is controlled using predefined keywords such as Login, Click, EnterText, and Logout. Non-technical team members can create tests using these keywords.

### Advantage

- Easy for non-programmers.

### Disadvantage

- Framework design is more complex.

### Course Management Example

Business analysts prepare keyword sheets while automation engineers implement the keywords.

---

## 5. Hybrid Framework

### Description

The Hybrid Framework combines the features of Modular, Data-Driven, and Keyword-Driven frameworks.

### Advantage

- Flexible, reusable, and scalable.

### Disadvantage

- More complex to develop initially.

### Course Management Example

- Modular Page Objects
- Excel or JSON test data
- Reusable utilities
- Shared login module
- Configuration file

---

# 2. Recommended Framework

## Scenario

The team needs to:

- Test login using 50 username/password combinations.
- Reuse login functionality in multiple test cases.
- Support both technical and non-technical team members.

### Recommendation

A **Hybrid Framework** is the best choice because it combines:

- Modular Framework for reusable components.
- Data-Driven Framework for multiple login datasets.
- Keyword-Driven Framework for business-friendly test creation.

This approach improves maintainability, scalability, and collaboration.

---

# 3. Hybrid Framework Folder Structure

```
CourseManagementAutomation/
│
├── config/
│   └── config.py
│
├── data/
│   ├── login_data.xlsx
│   └── course_data.xlsx
│
├── pages/
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── course_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_create_course.py
│   └── test_delete_course.py
│
├── utilities/
│   ├── browser.py
│   ├── logger.py
│   └── helpers.py
│
├── reports/
│
└── README.md
```

---

# Benefits of a Hybrid Framework

- Reusable code
- Easy maintenance
- Supports multiple test data sets
- Easy to scale
- Suitable for large automation projects