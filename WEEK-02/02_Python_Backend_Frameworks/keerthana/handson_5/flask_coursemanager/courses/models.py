from extensions import db


# Department Model
class Department(db.Model):

    __tablename__ = "departments"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    courses = db.relationship(
        "Course",
        back_populates="department",
        cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }


# Course Model
class Course(db.Model):

    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    code = db.Column(db.String(20), unique=True, nullable=False)

    credits = db.Column(db.Integer, nullable=False)

    department_id = db.Column(
        db.Integer,
        db.ForeignKey("departments.id"),
        nullable=False
    )

    department = db.relationship(
        "Department",
        back_populates="courses"
    )

    enrollments = db.relationship(
        "Enrollment",
        back_populates="course",
        cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "credits": self.credits,
            "department_id": self.department_id
        }


# Student Model
class Student(db.Model):

    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(100), unique=True)

    enrollments = db.relationship(
        "Enrollment",
        back_populates="student",
        cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }


# Enrollment Model
class Enrollment(db.Model):

    __tablename__ = "enrollments"

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id")
    )

    course_id = db.Column(
        db.Integer,
        db.ForeignKey("courses.id")
    )

    student = db.relationship(
        "Student",
        back_populates="enrollments"
    )

    course = db.relationship(
        "Course",
        back_populates="enrollments"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "course_id": self.course_id
        }