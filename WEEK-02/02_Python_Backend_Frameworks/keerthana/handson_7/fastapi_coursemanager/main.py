from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    status,
    BackgroundTasks,
    Response,
)

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import engine, get_db
from models import Base, Course, Student, Enrollment, Department
from schemas import (
    DepartmentCreate,
    DepartmentResponse,
    CourseCreate,
    CourseUpdate,
    CourseResponse,
    StudentCreate,
    StudentResponse,
    EnrollmentCreate,
    EnrollmentResponse,
)

app = FastAPI(
    title="Course Management API",
    description="FastAPI CRUD API for Courses, Students and Enrollments",
    version="1.0",
    contact={
        "name": "Keerthana",
        "email": "keerthana@example.com",
    },
)


# ---------------------------------------------------
# Create Tables
# ---------------------------------------------------

@app.on_event("startup")
async def startup():

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# ---------------------------------------------------
# Root
# ---------------------------------------------------

@app.get("/")
async def root():
    return {"message": "API Running Successfully"}


# ===================================================
# COURSES
# ===================================================

@app.post(
    "/api/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Courses"],
    summary="Create Course",
    response_description="New course created successfully",
)
async def create_course(
    course: CourseCreate,
    db: AsyncSession = Depends(get_db),
):

    new_course = Course(
        name=course.name,
        code=course.code,
        credits=course.credits,
        department_id=course.department_id,
    )

    db.add(new_course)

    await db.commit()

    await db.refresh(new_course)

    return new_course


@app.get(
    "/api/courses/",
    response_model=list[CourseResponse],
    tags=["Courses"],
)
async def get_courses(
    db: AsyncSession = Depends(get_db),
):

    result = await db.execute(select(Course))

    return result.scalars().all()


@app.get(
    "/api/courses/{course_id}",
    response_model=CourseResponse,
    tags=["Courses"],
)
async def get_course(
    course_id: int,
    db: AsyncSession = Depends(get_db),
):

    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found",
        )

    return course


@app.put(
    "/api/courses/{course_id}",
    response_model=CourseResponse,
    tags=["Courses"],
)
async def update_course(
    course_id: int,
    updated: CourseUpdate,
    db: AsyncSession = Depends(get_db),
):

    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found",
        )

    if updated.name is not None:
        course.name = updated.name

    if updated.code is not None:
        course.code = updated.code

    if updated.credits is not None:
        course.credits = updated.credits

    if updated.department_id is not None:
        course.department_id = updated.department_id

    await db.commit()

    await db.refresh(course)

    return course


@app.delete(
    "/api/courses/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Courses"],
)
async def delete_course(
    course_id: int,
    db: AsyncSession = Depends(get_db),
):

    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found",
        )

    await db.delete(course)

    await db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


# ===================================================
# STUDENTS
# ===================================================

@app.post(
    "/api/students/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Students"],
)
async def create_student(
    student: StudentCreate,
    db: AsyncSession = Depends(get_db),
):

    new_student = Student(
        name=student.name,
        email=student.email,
    )

    db.add(new_student)

    await db.commit()

    await db.refresh(new_student)

    return new_student


@app.get(
    "/api/students/",
    response_model=list[StudentResponse],
    tags=["Students"],
)
async def get_students(
    db: AsyncSession = Depends(get_db),
):

    result = await db.execute(select(Student))

    return result.scalars().all()


# ===================================================
# Background Task
# ===================================================

def send_confirmation_email(student_email: str):
    print(f"Sending confirmation to {student_email}")


# ===================================================
# ENROLLMENTS
# ===================================================

@app.post(
    "/api/enrollments/",
    response_model=EnrollmentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Enrollments"]
)
async def create_enrollment(
    enrollment: EnrollmentCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
):

    student = await db.get(Student, enrollment.student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    course = await db.get(Course, enrollment.course_id)

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found",
        )

    new_enrollment = Enrollment(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id,
    )

    db.add(new_enrollment)

    await db.commit()

    await db.refresh(new_enrollment)

    background_tasks.add_task(
        send_confirmation_email,
        student.email,
    )

    return new_enrollment


@app.get(
    "/api/courses/{course_id}/students/",
    response_model=list[StudentResponse],
    tags=["Courses"],
)
async def get_course_students(
    course_id: int,
    db: AsyncSession = Depends(get_db),
):

    result = await db.execute(
        select(Student)
        .join(Enrollment)
        .where(Enrollment.course_id == course_id)
    )

    return result.scalars().all()

#------------------------------------
@app.post(
    "/api/departments/",
    response_model=DepartmentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Departments"],
)
async def create_department(
    department: DepartmentCreate,
    db: AsyncSession = Depends(get_db),
):

    new_department = Department(
        name=department.name
    )

    db.add(new_department)

    await db.commit()

    await db.refresh(new_department)

    return new_department

@app.get(
    "/api/departments/",
    response_model=list[DepartmentResponse],
    tags=["Departments"],
)
async def get_departments(
    db: AsyncSession = Depends(get_db),
):

    result = await db.execute(
        select(Department)
    )

    return result.scalars().all()

@app.get(
    "/api/departments/{department_id}",
    response_model=DepartmentResponse,
    tags=["Departments"],
)
async def get_department(
    department_id: int,
    db: AsyncSession = Depends(get_db),
):

    result = await db.execute(
        select(Department).where(
            Department.id == department_id
        )
    )

    department = result.scalar_one_or_none()

    if department is None:
        raise HTTPException(
            status_code=404,
            detail="Department not found",
        )

    return department

@app.put(
    "/api/departments/{department_id}",
    response_model=DepartmentResponse,
    tags=["Departments"],
)
async def update_department(
    department_id: int,
    department: DepartmentCreate,
    db: AsyncSession = Depends(get_db),
):

    result = await db.execute(
        select(Department).where(
            Department.id == department_id
        )
    )

    existing_department = result.scalar_one_or_none()

    if existing_department is None:
        raise HTTPException(
            status_code=404,
            detail="Department not found",
        )

    existing_department.name = department.name

    await db.commit()

    await db.refresh(existing_department)

    return existing_department

@app.delete(
    "/api/departments/{department_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Departments"],
)
async def delete_department(
    department_id: int,
    db: AsyncSession = Depends(get_db),
):

    result = await db.execute(
        select(Department).where(
            Department.id == department_id
        )
    )

    department = result.scalar_one_or_none()

    if department is None:
        raise HTTPException(
            status_code=404,
            detail="Department not found",
        )

    await db.delete(department)

    await db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)