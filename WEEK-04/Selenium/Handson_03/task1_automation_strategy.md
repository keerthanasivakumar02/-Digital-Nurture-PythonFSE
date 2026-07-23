# Task 1 - Automation Decision and Test Case Selection

## Objective

Understand how to decide which test cases should be automated, calculate Automation ROI, and identify flaky tests.

---

# 1. Criteria for Automating Test Cases

## Criterion 1 - Repetitive Test

Tests that are executed frequently are good candidates for automation.

**Application to Course Management API:**

The `POST /api/courses/` endpoint is tested every release, so automating it saves time.

---

## Criterion 2 - Regression Test

Regression tests verify that existing functionality still works after code changes.

**Application:**

The course creation API should be automated because it is part of every regression cycle.

---

## Criterion 3 - Stable Functionality

Automation is suitable for features that do not change frequently.

**Application:**

The API endpoint for creating courses has a stable request and response structure.

---

## Criterion 4 - Data-Driven Testing

Automation is effective when the same test must run with multiple data sets.

**Application:**

Test the course creation API using different course codes and names.

---

## Criterion 5 - High Business Risk

Critical business functionality should always be automated.

**Application:**

If course creation fails, students cannot enroll. Therefore, it is a high-priority automation candidate.

---

# 2. Manual vs Automation Decision

| Test Case | Decision | Reason |
|-----------|----------|--------|
| Regression test for CRUD APIs | Automate | Runs after every code change |
| Exploratory testing of new search | Manual | Requires human observation |
| Performance test (100 users) | Automate | Performance tools execute repetitive load tests |
| Login UI test | Automate | Frequently executed regression test |
| Swagger documentation verification | Manual | Mostly visual review |
| Smoke test after deployment | Automate | Fast verification after deployment |

---

# 3. Automation ROI

## Definition

Automation ROI (Return on Investment) measures when the effort spent creating automated tests becomes worthwhile compared to manual execution.

---

## Calculation

Automation Time = 4 hours

Manual Execution Time = 30 minutes (0.5 hours)

Break-even Runs:

4 ÷ 0.5 = 8 runs

Therefore, after **8 executions**, automation starts saving time.

### Maintenance

After the 10th run, each execution requires a maintenance effort of 20%.

Even with maintenance, automation remains more efficient for long-term regression testing.

---

# 4. Flaky Tests

## Definition

A flaky test is a test that sometimes passes and sometimes fails without any changes to the application.

---

## Example

A Selenium test clicks the Login button before the page has fully loaded.

Sometimes it passes.

Sometimes it fails.

---

## Preventing Flaky Tests

1. Use Explicit Waits instead of Thread.sleep().
2. Use reliable locators (ID, Name, CSS Selector).
3. Ensure the test environment is stable before execution.

---

# Conclusion

Good automation focuses on repetitive, stable, regression, data-driven, and high-risk test cases. A reliable automation suite provides long-term time savings and improves software quality.