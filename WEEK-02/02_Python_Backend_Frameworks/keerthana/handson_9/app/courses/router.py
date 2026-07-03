from fastapi import APIRouter, Depends, HTTPException

from app.schemas import CourseCreate
from app.database import courses
from app.auth.dependencies import get_current_user

router = APIRouter(
    prefix="/api/v1/courses",
    tags=["Courses"]
)


# Public Endpoint
@router.get("/")
def get_courses():
    return courses


# Protected Endpoint
@router.post("/")
def create_course(
    course: CourseCreate,
    current_user=Depends(get_current_user)
):

    new_course = {
        "id": len(courses) + 1,
        "title": course.title,
        "description": course.description
    }

    courses.append(new_course)

    return {
        "message": "Course created successfully",
        "course": new_course
    }


# Protected Endpoint
@router.delete("/{course_id}")
def delete_course(
    course_id: int,
    current_user=Depends(get_current_user)
):

    for course in courses:

        if course["id"] == course_id:
            courses.remove(course)

            return {
                "message": "Course deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )