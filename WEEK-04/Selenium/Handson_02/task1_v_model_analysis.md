# Task 1 - SDLC vs TDLC (V-Model Mapping)

## Objective

Understand how Software Development Life Cycle (SDLC) phases are mapped to Software Testing Life Cycle (TDLC) phases using the V-Model.

---

# V-Model

```
                    SDLC                           TDLC

         Requirements -----------------> Acceptance Testing
                |                                 ^
                |                                 |
         System Design ----------------> System Testing
                |                                 ^
                |                                 |
     Architecture Design -------------> Integration Testing
                |                                 ^
                |                                 |
         Module Design ---------------> Unit Testing
                |                                 ^
                |                                 |
                     \                           /
                      \                         /
                           Coding
```

---

# SDLC Phase Mapping

| SDLC Phase | Corresponding TDLC Phase | Test Artifact Produced |
|------------|---------------------------|------------------------|
| Requirements | Acceptance Testing | Acceptance Test Plan |
| System Design | System Testing | System Test Cases |
| Architecture Design | Integration Testing | Integration Test Plan |
| Module Design | Unit Testing | Unit Test Cases |
| Coding | Test Execution | Executable Software |

---

# Entry and Exit Criteria

## 1. Unit Testing

### Entry Criteria

- Module is developed.
- Source code is available.
- Unit test cases are prepared.

### Exit Criteria

- All unit tests executed.
- Critical defects fixed.
- Code coverage achieved.

---

## 2. Integration Testing

### Entry Criteria

- Unit testing completed.
- Modules integrated.
- Integration test cases prepared.

### Exit Criteria

- Module interactions verified.
- Integration defects fixed.
- No critical integration issues.

---

## 3. System Testing

### Entry Criteria

- Entire application integrated.
- System test cases prepared.
- Test environment ready.

### Exit Criteria

- Functional testing completed.
- Critical defects fixed.
- Test summary prepared.

---

## 4. Acceptance Testing

### Entry Criteria

- System testing completed.
- Client requirements available.
- Acceptance test cases prepared.

### Exit Criteria

- Client approves the application.
- Business requirements satisfied.
- Application ready for release.

---

# QA Engagement in the Course Management API Project

QA should not wait until testing begins. QA can participate in the following early phases:

### 1. Requirements Review

- Verify requirements are complete and testable.
- Identify ambiguous or missing requirements.
- Suggest measurable acceptance criteria.

### 2. Design Review

- Review API endpoints and database design.
- Ensure the design supports testing.
- Identify potential risks before development starts.

---

# Benefits of the V-Model

- Testing starts early.
- Defects are identified sooner.
- Better collaboration between developers and testers.
- Improved software quality.
- Reduced development cost.