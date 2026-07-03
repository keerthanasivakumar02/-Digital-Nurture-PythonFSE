from flask import Blueprint, request, jsonify
from extensions import db
from courses.models import Course, Student, Enrollment

courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)


def make_response_json(data, status_code=200):
    return jsonify({
        "status": "success",
        "data": data
    }), status_code


# GET all courses
@courses_bp.route("/", methods=["GET"])
def get_courses():

    courses = Course.query.all()

    return make_response_json(
        [course.to_dict() for course in courses]
    )


# POST create course
@courses_bp.route("/", methods=["POST"])
def create_course():

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request must be JSON"}), 400

    required = ["name", "code", "credits", "department_id"]

    for field in required:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    course = Course(
        name=data["name"],
        code=data["code"],
        credits=data["credits"],
        department_id=data["department_id"]
    )

    db.session.add(course)
    db.session.commit()

    return make_response_json(
        course.to_dict(),
        201
    )


# GET course by id
@courses_bp.route("/<int:id>", methods=["GET"])
def get_course(id):

    course = Course.query.get_or_404(id)

    return make_response_json(
        course.to_dict()
    )


# UPDATE course
@courses_bp.route("/<int:id>", methods=["PUT"])
def update_course(id):

    course = Course.query.get_or_404(id)

    data = request.get_json()

    if "name" in data:
        course.name = data["name"]

    if "code" in data:
        course.code = data["code"]

    if "credits" in data:
        course.credits = data["credits"]

    if "department_id" in data:
        course.department_id = data["department_id"]

    db.session.commit()

    return make_response_json(
        course.to_dict()
    )


# DELETE course
@courses_bp.route("/<int:id>", methods=["DELETE"])
def delete_course(id):

    course = Course.query.get_or_404(id)

    db.session.delete(course)

    db.session.commit()

    return make_response_json(
        {"message": "Course deleted"}
    )


# JOIN query
@courses_bp.route("/<int:id>/students/", methods=["GET"])
def get_students(id):

    Course.query.get_or_404(id)

    students = (
        db.session.query(Student)
        .join(Enrollment)
        .filter(Enrollment.course_id == id)
        .all()
    )

    return make_response_json(
        [student.to_dict() for student in students]
    )