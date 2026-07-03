from flask import Flask, request, jsonify
import sqlite3
import requests
from requests.exceptions import ConnectionError

app = Flask(__name__)

DATABASE = "database.db"


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


init_db()


@app.route("/")
def home():
    return jsonify({
        "message": "Student Service Running"
    })


# Create Student
@app.route("/api/students", methods=["POST"])
def create_student():

    data = request.get_json()

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students(name, department) VALUES (?, ?)",
        (data["name"], data["department"])
    )

    conn.commit()

    student_id = cursor.lastrowid

    conn.close()

    return jsonify({
        "message": "Student created successfully",
        "id": student_id
    }), 201


# Get All Students
@app.route("/api/students", methods=["GET"])
def get_students():

    conn = get_connection()

    students = conn.execute(
        "SELECT * FROM students"
    ).fetchall()

    conn.close()

    return jsonify([
        dict(student)
        for student in students
    ])


# Get Student by ID
@app.route("/api/students/<int:student_id>", methods=["GET"])
def get_student(student_id):

    conn = get_connection()

    student = conn.execute(
        "SELECT * FROM students WHERE id=?",
        (student_id,)
    ).fetchone()

    conn.close()

    if student is None:
        return jsonify({
            "message": "Student not found"
        }), 404

    return jsonify(dict(student))
# Student Enrollment
@app.route("/api/students/<int:student_id>/enroll", methods=["POST"])
def enroll_student(student_id):

    data = request.get_json()

    course_id = data["course_id"]

    try:

        response = requests.get(
            f"http://127.0.0.1:5001/api/courses/{course_id}"
        )

    except ConnectionError:

        return jsonify({
            "message": "Course Service is unavailable"
        }), 503

    if response.status_code != 200:

        return jsonify({
            "message": "Course not found"
        }), 404

    return jsonify({
        "message": "Student enrolled successfully",
        "student_id": student_id,
        "course": response.json()
    })
if __name__ == "__main__":
    app.run(port=5002, debug=True)