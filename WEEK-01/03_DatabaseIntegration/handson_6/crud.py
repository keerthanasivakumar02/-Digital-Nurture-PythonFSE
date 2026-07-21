from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload

from models import (
    Base,
    Department,
    Student,
    Course,
    Enrollment,
    Professor,
)

DATABASE_URL = "mysql+mysqlconnector://root:keerthana%402004@localhost:3306/college_db_orm"

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

# ----------------------------
# Insert Departments
# ----------------------------

cs = Department(dept_name="Computer Science")
it = Department(dept_name="Information Technology")
ece = Department(dept_name="Electronics")

session.add_all([cs, it, ece])
session.commit()

# ----------------------------
# Insert Students
# ----------------------------

students = [

Student(
first_name="Arun",
last_name="Kumar",
email="arun@gmail.com",
enrollment_year=2022,
department=cs
),

Student(
first_name="Priya",
last_name="Sharma",
email="priya@gmail.com",
enrollment_year=2022,
department=cs
),

Student(
first_name="Rahul",
last_name="Verma",
email="rahul@gmail.com",
enrollment_year=2023,
department=it
),

Student(
first_name="Sneha",
last_name="Rao",
email="sneha@gmail.com",
enrollment_year=2023,
department=ece
),

Student(
first_name="Vijay",
last_name="Kumar",
email="vijay@gmail.com",
enrollment_year=2022,
department=cs
)

]

session.add_all(students)
session.commit()

# ----------------------------
# Insert Courses
# ----------------------------

course1 = Course(
course_code="CS101",
course_name="Database Systems",
credits=4
)

course2 = Course(
course_code="CS102",
course_name="Python Programming",
credits=3
)

course3 = Course(
course_code="CS103",
course_name="Operating Systems",
credits=4
)

session.add_all([course1, course2, course3])
session.commit()

# ----------------------------
# Insert Enrollments
# ----------------------------

enrollments = [

Enrollment(student=students[0], course=course1, grade="A"),

Enrollment(student=students[1], course=course2, grade="B"),

Enrollment(student=students[2], course=course3, grade="A"),

Enrollment(student=students[4], course=course1, grade="A+")

]

session.add_all(enrollments)
session.commit()

print("Data inserted successfully.")


# ----------------------------
# READ - Students in Computer Science
# ----------------------------

print("\nStudents in Computer Science Department:")

students_cs = (
    session.query(Student)
    .join(Department)
    .filter(Department.dept_name == "Computer Science")
    .all()
)

for student in students_cs:
    print(student.first_name, student.last_name)

    # ----------------------------
# READ - Enrollments
# ----------------------------

print("\nOptimized Student Enrollments:")

enrollments = (
    session.query(Enrollment)
    .options(
        joinedload(Enrollment.student),
        joinedload(Enrollment.course)
    )
    .all()
)

for enrollment in enrollments:
    print(
        enrollment.student.first_name,
        "-",
        enrollment.course.course_name,
        "- Grade:",
        enrollment.grade
    )
    # ----------------------------
# UPDATE
# ----------------------------

student = session.query(Student).filter_by(email="arun@gmail.com").first()

if student:
    student.enrollment_year = 2024
    session.commit()
    print("\nStudent Updated Successfully!")

    """
Step 87 Observation

Without joinedload(),
SQLAlchemy executes multiple SQL queries.

One query retrieves enrollments.
Additional queries retrieve each student.
Additional queries retrieve each course.

This is called the N+1 Query Problem.
"""

"""
Step 89 Observation

Using joinedload(),

Student and Course data are fetched together
using SQL JOINs.

Database queries reduced from
multiple queries to a single query.

Performance improved.
"""

"""
Task 3 Comparison

Before joinedload()

• One query fetched enrollments.
• Additional queries fetched students.
• Additional queries fetched courses.
• Multiple SQL statements were executed.

After joinedload()

• One SQL JOIN query fetched
  Enrollment, Student and Course data.

Result:

N+1 Query Problem Eliminated.
Performance Improved.
"""

"""
Bonus

Django ORM equivalent:

Enrollment.objects.select_related(
    "student",
    "course"
).all()
"""