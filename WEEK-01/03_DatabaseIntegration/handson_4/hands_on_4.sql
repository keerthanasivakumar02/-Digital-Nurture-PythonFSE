
use college_db
EXPLAIN FORMAT=JSON

SELECT
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;

EXPLAIN FORMAT=JSON

SELECT
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;

/*
Step 48 - EXPLAIN FORMAT=JSON Analysis

Students Table:
- Access Type: ALL (Full Table Scan)

Enrollments Table:
- Access Type: ref

Courses Table:
- Access Type: eq_ref

Observation:
No index exists on enrollment_year.
Therefore, MySQL performs a full table scan on the students table.
This may reduce query performance as the table grows.
*/

CREATE INDEX idx_students_enrollment_year
ON students(enrollment_year);

CREATE UNIQUE INDEX idx_enrollments_student_course
ON enrollments(student_id, course_id);

CREATE INDEX idx_courses_course_code
ON courses(course_code);

EXPLAIN FORMAT=JSON

SELECT
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;

/*
Task 2 – Index Analysis

Indexes Created:
1. idx_students_enrollment_year
2. idx_enrollments_student_course

Observations:
- The index on enrollment_year improves filtering performance.
- The composite index speeds up JOIN operations.
- EXPLAIN FORMAT=JSON shows that MySQL uses the created indexes.
- Query cost is reduced compared to the execution plan before indexing.
*/

/*
Step 58 – Compare Database Round-Trips

---------------------------------------------------------
Approach                  | Queries Executed
---------------------------------------------------------
N+1 Query                 | 1 + N Queries
Optimized JOIN            | 1 Query
---------------------------------------------------------

Observation:
The JOIN approach minimizes database round-trips and
significantly improves performance by retrieving all
required data in a single query.
*/

/*
Step 59 – Explain the N+1 Query Problem

The N+1 Query Problem occurs when:

1. One query retrieves N records.
2. An additional query is executed for each record.
3. Total database queries become N + 1.

Examples:

10 enrollments   -> 11 queries
100 enrollments  -> 101 queries
1000 enrollments -> 1001 queries

Using a single JOIN query retrieves all required data
in one database call, eliminating unnecessary database
round-trips and improving application performance.

Learning Outcomes:
- Analyzed SQL execution plans using EXPLAIN FORMAT=JSON.
- Identified full table scans and estimated rows examined.
- Improved query performance using B-Tree and composite indexes.
- Understood the impact of indexes on query execution plans.
- Learned the MySQL alternative to partial indexes.
- Identified and resolved the N+1 Query Problem.
- Compared database round-trips before and after optimization.
- Optimized database access using SQL JOIN operations.
*/