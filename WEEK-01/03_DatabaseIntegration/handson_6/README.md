# Hands-On 6 – ORM Integration using SQLAlchemy

## 📚 Module

**Digital Nurture 5.0 – Python Full Stack Engineer**

**Module 3:** Database Integration – PostgreSQL, MySQL & MongoDB


---

## 🎯 Objective

The objective of this hands-on is to understand Object Relational Mapping (ORM) using SQLAlchemy by creating database models, performing CRUD operations, defining relationships between tables, and optimizing database queries using eager loading (`joinedload`) to eliminate the N+1 query problem.

---

## 🛠 Technologies Used

- Python 3
- SQLAlchemy ORM
- MySQL
- MySQL Connector
- VS Code

---

## 📦 Python Packages

```bash
pip install sqlalchemy mysql-connector-python
```

---

## 📂 Files Included

```text
Handson_6/
│── models.py
│── crud.py
│── README.md
```

---

## 📌 Tasks Completed

### Task 1 – SQLAlchemy Models

- Connected SQLAlchemy to the MySQL database.
- Created the `college_db_orm` database.
- Defined ORM models for:
  - Department
  - Student
  - Course
  - Enrollment
  - Professor
- Established relationships using SQLAlchemy ORM.
- Created database tables automatically using `Base.metadata.create_all(engine)`.

---

### Task 2 – CRUD Operations

#### Create

- Inserted Department records.
- Inserted Student records.
- Inserted Course records.
- Inserted Enrollment records.

#### Read

- Retrieved all students belonging to the **Computer Science** department.
- Retrieved enrollment details along with student names and course names.

#### Update

- Updated a student's enrollment year using SQLAlchemy Session.

#### Delete

- Deleted an enrollment record using the ORM.

---

### Task 3 – Solving the N+1 Query Problem

- Enabled SQL query logging using `echo=True`.
- Observed multiple SQL queries generated during lazy loading.
- Optimized the query using `joinedload()`.
- Retrieved Enrollment, Student, and Course data using a single SQL query.
- Compared query execution before and after optimization.

---

## 📖 SQLAlchemy Concepts Practiced

- ORM Mapping
- Declarative Base
- Engine Configuration
- Sessions
- CRUD Operations
- One-to-Many Relationships
- Many-to-One Relationships
- Foreign Keys
- Lazy Loading
- Eager Loading
- `joinedload()`
- Query Optimization

---

## 🎯 Learning Outcomes

After completing this hands-on, I was able to:

- Connect Python applications to MySQL using SQLAlchemy.
- Create ORM model classes.
- Define relationships between database tables.
- Perform Create, Read, Update, and Delete operations using ORM.
- Manage database transactions with SQLAlchemy Sessions.
- Identify the N+1 Query Problem.
- Optimize database queries using `joinedload()`.
- Improve application performance by reducing unnecessary SQL queries.

---

## 🚀 Key Skills Gained

- SQLAlchemy ORM
- Database Modeling
- Object Relational Mapping (ORM)
- CRUD Operations
- Session Management
- Relationship Mapping
- Query Optimization
- Eager Loading
- Python Database Programming
- MySQL Integration

---

## 📈 Expected Outcome

Successfully created an ORM-based application that:

- Models the college database using SQLAlchemy.
- Performs CRUD operations without writing raw SQL.
- Uses relationships to access related data.
- Eliminates the N+1 Query Problem using eager loading (`joinedload()`).
- Improves database performance through optimized queries.

---

## ✅ Status

✔ Hands-On 6 Completed Successfully


---

## 👩‍💻 Author

**KeerthanaSivakumar**