from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

COURSE_SERVICE = "http://127.0.0.1:5001"
STUDENT_SERVICE = "http://127.0.0.1:5002"


# Home
@app.route("/")
def home():
    return jsonify({
        "message": "API Gateway Running"
    })


# Forward Course Requests
@app.route("/api/courses", methods=["GET", "POST"])
def courses():

    response = requests.request(
        method=request.method,
        url=f"{COURSE_SERVICE}/api/courses",
        json=request.get_json(silent=True)
    )

    return (
        response.content,
        response.status_code,
        response.headers.items()
    )


# Forward Course by ID
@app.route("/api/courses/<int:course_id>", methods=["GET"])
def course_by_id(course_id):

    response = requests.get(
        f"{COURSE_SERVICE}/api/courses/{course_id}"
    )

    return (
        response.content,
        response.status_code,
        response.headers.items()
    )


# Forward Student Requests
@app.route("/api/students", methods=["GET", "POST"])
def students():

    response = requests.request(
        method=request.method,
        url=f"{STUDENT_SERVICE}/api/students",
        json=request.get_json(silent=True)
    )

    return (
        response.content,
        response.status_code,
        response.headers.items()
    )


# Forward Enrollment Request
@app.route("/api/students/<int:student_id>/enroll", methods=["POST"])
def enroll(student_id):

    response = requests.post(
        f"{STUDENT_SERVICE}/api/students/{student_id}/enroll",
        json=request.get_json()
    )

    return (
        response.content,
        response.status_code,
        response.headers.items()
    )


if __name__ == "__main__":
    app.run(port=5000, debug=True)