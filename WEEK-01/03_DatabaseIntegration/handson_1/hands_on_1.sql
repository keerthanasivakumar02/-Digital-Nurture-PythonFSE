CREATE DATABASE college_db;
USE college_db;
CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL,
    hod_name VARCHAR(100),
    budget DECIMAL(12,2)
);
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    date_of_birth DATE,
    department_id INT,
    enrollment_year INT,
    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
);
CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(150) NOT NULL,
    course_code VARCHAR(20) UNIQUE,
    credits INT,
    department_id INT,
    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
);
CREATE TABLE professors (
    professor_id INT AUTO_INCREMENT PRIMARY KEY,
    prof_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    department_id INT,
    salary DECIMAL(10,2),
    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
);
CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    grade CHAR(2),
    FOREIGN KEY (student_id)
    REFERENCES students(student_id),
    FOREIGN KEY (course_id)
    REFERENCES courses(course_id)
);
SHOW TABLES;
DESCRIBE departments;
DESCRIBE students;
DESCRIBE courses;
DESCRIBE enrollments;
DESCRIBE professors;

ALTER TABLE students
ADD phone_number VARCHAR(15);

ALTER TABLE courses
ADD max_seats INT DEFAULT 60;

ALTER TABLE enrollments
ADD CONSTRAINT chk_grade
CHECK (grade IN ('A','B','C','D','F') OR grade IS NULL);

ALTER TABLE departments
CHANGE COLUMN hod_name  head_of_dept VARCHAR(100);

ALTER TABLE students
DROP COLUMN phone_number;

DESCRIBE departments;
DESCRIBE courses;
DESCRIBE students;
DESCRIBE enrollments;

-- ==========================================
-- Normalization Analysis
-- ==========================================

-- 1NF (First Normal Form)
-- All tables contain atomic values.
-- Each column stores only one value.
-- There are no repeating groups or multi-valued attributes.
-- Example: phone numbers are not stored as multiple values in one column.

-- 2NF (Second Normal Form)
-- All non-key attributes are fully dependent on the primary key.
-- In the enrollments table, student_id and course_id identify a student's enrollment.
-- Attributes like enrollment_date and grade depend on the entire enrollment record.
-- Therefore, there are no partial dependencies.

-- 3NF (Third Normal Form)
-- No non-key attribute depends on another non-key attribute.
-- Department information is stored in the departments table.
-- The students table stores only department_id instead of dept_name.
-- This avoids transitive dependency and satisfies 3NF.

-- Enrollments Table 3NF Analysis
-- The enrollments table stores only enrollment-related information.
-- Student details are stored in students.
-- Course details are stored in courses.
-- Therefore, the table satisfies Third Normal Form.

