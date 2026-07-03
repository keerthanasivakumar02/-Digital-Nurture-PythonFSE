from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class Base(DeclarativeBase):
    pass


class Department(Base):

    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    courses = relationship("Course", back_populates="department")


class Course(Base):

    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    code: Mapped[str]
    credits: Mapped[int]

    department_id: Mapped[int] = mapped_column(
        ForeignKey("departments.id")
    )

    department = relationship(
        "Department",
        back_populates="courses"
    )

    enrollments = relationship(
        "Enrollment",
        back_populates="course"
    )


class Student(Base):

    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]

    enrollments = relationship(
        "Enrollment",
        back_populates="student"
    )


class Enrollment(Base):

    __tablename__ = "enrollments"

    id: Mapped[int] = mapped_column(primary_key=True)

    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id")
    )

    course_id: Mapped[int] = mapped_column(
        ForeignKey("courses.id")
    )

    student = relationship(
        "Student",
        back_populates="enrollments"
    )

    course = relationship(
        "Course",
        back_populates="enrollments"
    )