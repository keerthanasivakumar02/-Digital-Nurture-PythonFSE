# Hands-On 4 – Query Optimization (Indexes, EXPLAIN & N+1 Query Problem)

## 📚 Module

**Digital Nurture 5.0 – Python Full Stack Engineer**

**Module 3:** Database Integration – PostgreSQL, MySQL & MongoDB


---

## 🎯 Objective

The objective of this hands-on is to understand SQL query optimization techniques by analyzing query execution plans, creating indexes, and identifying the N+1 Query Problem using SQL and Python.

---

## 🛠 Technologies Used

- MySQL 8.x
- MySQL Workbench
- Python 3.x
- MySQL Connector for Python
- SQL

---

## 📂 Files Included

```
Hands-On-4/
│── hands_on_4.sql
│── step56.py
│── step57.py
│── README.md
```

---

## 📌 Tasks Completed

### Task 1 – Analyze Query Execution Plan

Performed query performance analysis using:

- `EXPLAIN FORMAT=JSON`
- Query execution plan analysis
- Query cost estimation
- Table scan identification

Activities completed:

- Executed `EXPLAIN FORMAT=JSON`
- Identified full table scans
- Examined query execution details before optimization

---

### Task 2 – Query Optimization Using Indexes

Created indexes to improve database performance.

Indexes Created:

- Single-column index on `students(enrollment_year)`
- Composite index on `enrollments(student_id, course_id)`

Activities completed:

- Created and verified indexes
- Compared execution plans before and after indexing
- Observed reduced query cost and improved index usage

---

### Task 3 – Identify and Fix the N+1 Query Problem

Implemented Python programs to demonstrate database performance.

Files Created:

- `step56.py` – Simulated the N+1 Query Problem
- `step57.py` – Optimized the query using SQL JOIN

Activities completed:

- Connected Python with MySQL
- Counted database queries in the N+1 approach
- Eliminated unnecessary database round-trips using JOIN
- Compared query execution efficiency

---

## 📖 Concepts Practiced

- Query Optimization
- EXPLAIN FORMAT=JSON
- Query Execution Plans
- Full Table Scan Analysis
- B-Tree Indexes
- Composite Indexes
- MySQL Index Optimization
- Python MySQL Connectivity
- N+1 Query Problem
- SQL JOIN Optimization
- Database Performance Tuning

---

## 🎯 Learning Outcomes

After completing this hands-on, I gained practical experience in:

- Analyzing SQL query execution plans using `EXPLAIN FORMAT=JSON`.
- Identifying full table scans and understanding query cost.
- Improving SQL query performance using indexes.
- Creating and using single-column and composite indexes.
- Connecting Python applications with MySQL databases.
- Demonstrating the N+1 Query Problem using Python.
- Optimizing database access using SQL JOIN operations.
- Comparing database round-trips before and after optimization.

---

## 🚀 Key Skills Gained

- SQL Query Optimization
- Database Performance Analysis
- Index Creation
- Execution Plan Interpretation
- Python Database Programming
- MySQL Connector
- JOIN Optimization
- Performance Tuning

---

## ✅ Status

✔ Hands-On 4 Completed Successfully

---

## 👩‍💻 Author

**KeerthanaSivakumar**