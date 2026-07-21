# Hands-On 3 – Advanced SQL (Subqueries, Views, Stored Procedures & Transactions)

## 📚 Module
**Digital Nurture 5.0 – Python Full Stack Engineer**

**Module 3:** Database Integration – PostgreSQL, MySQL & MongoDB


---

## 🎯 Objective

The objective of this hands-on is to develop advanced SQL skills by working with:

- Subqueries
- Correlated & Non-Correlated Queries
- SQL Views
- Stored Procedures
- Transactions
- COMMIT
- ROLLBACK
- SAVEPOINT

The exercises were performed using the **Student Course Registration System** database created in the previous hands-on exercises.

---

## 🛠 Technologies Used

- MySQL 8.x
- MySQL Workbench
- SQL

---

## 📂 Files Included

```
Hands-On-3/
│── hands_on_3.sql
│── README.md
```

---

## 📌 Tasks Completed

### Task 1 – Advanced SQL Using Subqueries

Implemented SQL queries using:

- Non-Correlated Subqueries
- Correlated Subqueries
- Derived Tables
- EXISTS
- NOT EXISTS

Queries performed:

- Retrieved students enrolled in more courses than the average.
- Listed courses where every enrolled student received grade 'A'.
- Identified the highest-paid professor in each department.
- Calculated average professor salary by department using derived tables.

---

### Task 2 – Creating and Using Views

Created reusable SQL views for reporting purposes.

Views Created:

- `vw_student_enrollment_summary`
- `vw_course_stats`

Operations performed:

- Queried students with GPA greater than 3.0.
- Tested updating a multi-table view.
- Dropped existing views.
- Recreated a single-table view using `WITH CHECK OPTION`.

---

### Task 3 – Stored Procedures and Transactions

Implemented stored procedures to automate business operations.

Created Procedures:

- `sp_enroll_student`
- `sp_transfer_student`

Database transaction concepts practiced:

- START TRANSACTION
- COMMIT
- ROLLBACK
- SAVEPOINT
- Exception handling using `SIGNAL`

Additional implementation:

- Created `department_transfer_log` table to record department transfers.
- Prevented duplicate enrollments.
- Verified rollback functionality during transaction failures.

---

## 📖 SQL Concepts Practiced

- Subqueries
- Correlated Subqueries
- Derived Tables
- EXISTS / NOT EXISTS
- SQL Views
- WITH CHECK OPTION
- Stored Procedures
- Parameters
- IF Statements
- SIGNAL
- Transactions
- COMMIT
- ROLLBACK
- SAVEPOINT

---

## 🎯 Learning Outcome

After completing this hands-on, I gained practical experience in:

- Writing advanced SQL queries using subqueries.
- Creating reusable database views.
- Designing stored procedures for business logic.
- Managing database transactions safely.
- Handling exceptions within SQL procedures.
- Maintaining data integrity using COMMIT, ROLLBACK, and SAVEPOINT.

---

## 🚀 Key Skills Gained

- Advanced SQL Query Writing
- View Creation
- Stored Procedure Development
- Transaction Management
- Database Programming
- Error Handling
- Data Integrity
- Business Logic Implementation

---

## ✅ Status

✔ Hands-On 3 Completed Successfully

---

## 👩‍💻 Author

**Keerthana Sivakumar**