# Hands-On 7 – Migrations & Versioning using Alembic

## 📚 Module

**Digital Nurture 5.0 – Python Full Stack Engineer**

**Module 3:** Database Integration – PostgreSQL, MySQL & MongoDB



---

## 🎯 Objective

The objective of this hands-on is to understand database schema versioning and migration management using Alembic with SQLAlchemy. The exercise demonstrates creating migration scripts, updating database schemas, applying migrations, maintaining migration history, and performing rollback operations safely.

---

## 🛠 Technologies Used

- Python 3
- SQLAlchemy
- Alembic
- MySQL
- MySQL Connector
- VS Code

---

## 📦 Python Packages

```bash
pip install sqlalchemy
pip install alembic
pip install mysql-connector-python
```

---

## 📂 Project Structure

```text
Handson_7/
│── models.py
│── alembic.ini
│── migrations/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
│── README.md
```

---

# Tasks Completed

## Task 1 – Alembic Setup & Baseline Migration

### Completed Steps

- Installed Alembic.
- Initialized the Alembic project.
- Configured `alembic.ini` with the MySQL connection string.
- Configured `env.py` to use SQLAlchemy models.
- Generated the initial migration using autogeneration.
- Applied the migration to the database.
- Verified migration status using Alembic.

---

## Task 2 – Incremental Schema Changes

### Completed Steps

- Added the **is_active** column to the Student model.
- Generated a migration for the new column.
- Applied the migration successfully.
- Verified the column in MySQL.
- Added the **CourseSchedule** model.
- Generated a migration for the new table.
- Applied the migration.
- Verified the new table creation.
- Displayed the migration history.

---

## Task 3 – Rollback & Recovery

### Completed Steps

- Checked the current migration revision.
- Performed rollback to the previous migration.
- Rolled back to the base migration.
- Reapplied all migrations using **upgrade head**.
- Verified the latest schema version.

---

# Alembic Commands Used

## Initialize Alembic

```bash
python -m alembic init migrations
```

---

## Generate Initial Migration

```bash
python -m alembic revision --autogenerate -m "initial schema"
```

---

## Apply Migration

```bash
python -m alembic upgrade head
```

---

## View Current Migration

```bash
python -m alembic current
```

---

## View Migration History

```bash
python -m alembic history --verbose
```

---

## Generate New Migration

```bash
python -m alembic revision --autogenerate -m "add is_active to students"
```

```bash
python -m alembic revision --autogenerate -m "add course schedule table"
```

---

## Roll Back One Revision

```bash
python -m alembic downgrade -1
```

---

## Roll Back to Base

```bash
python -m alembic downgrade base
```

---

## Upgrade to Latest Version

```bash
python -m alembic upgrade head
```

---

# Concepts Learned

- Object Relational Mapping (ORM)
- SQLAlchemy Metadata
- Alembic Configuration
- Migration Generation
- Database Version Control
- Schema Evolution
- Upgrade and Downgrade Operations
- Migration History
- Rollback Strategy
- Database Recovery
- Auto-generated Migrations

---

# Learning Outcomes

After completing this hands-on, I was able to:

- Configure Alembic with SQLAlchemy.
- Generate migration scripts automatically.
- Apply migrations to a MySQL database.
- Modify an existing database schema safely.
- Add new tables and columns through migrations.
- Track migration history.
- Roll back database changes when required.
- Restore the latest schema using upgrade commands.
- Understand database version control in real-world applications.

---

# Key Skills Gained

- Alembic
- SQLAlchemy
- MySQL
- ORM
- Database Versioning
- Schema Migration
- Migration History
- Upgrade & Downgrade
- Database Administration
- Python Database Development

---

# Expected Outcome

Successfully implemented database schema versioning using Alembic by:

- Creating the initial database migration.
- Applying schema changes through migration scripts.
- Tracking migration history.
- Performing rollback and recovery operations.
- Maintaining synchronized database schema and application models.

---

# Screenshots Included

- Alembic Installation
- Alembic Initialization
- Initial Migration Generation
- Upgrade Head
- Current Migration
- Migration History
- MySQL Tables Verification
- Added `is_active` Column
- Created `course_schedules` Table
- Downgrade Operation
- Upgrade After Rollback

---

# Conclusion

This hands-on provided practical experience with Alembic migration workflows. It demonstrated how database schemas can evolve alongside application code while maintaining version history and enabling safe rollback and recovery mechanisms. These concepts are essential for managing production databases in enterprise software development.

---

## ✅ Status

**Hands-On 7 Completed Successfully**
**Digital Nurture 5.0 – Module 3**
**Author:** **KeerthanaSivakumar**