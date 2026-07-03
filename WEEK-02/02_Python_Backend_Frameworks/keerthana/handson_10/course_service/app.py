from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = "database.db"


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS courses (
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
        "message": "Course Service Running"
    })


# Create Course
@app.route("/api/courses", methods=["POST"])
def create_course():

    data = request.get_json()

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO courses (name, department) VALUES (?, ?)",
        (data["name"], data["department"])
    )

    conn.commit()

    course_id = cursor.lastrowid

    conn.close()

    return jsonify({
        "message": "Course created successfully",
        "id": course_id
    }), 201


# Get All Courses
@app.route("/api/courses", methods=["GET"])
def get_courses():

    conn = get_connection()

    courses = conn.execute(
        "SELECT * FROM courses"
    ).fetchall()

    conn.close()

    return jsonify([
        dict(course)
        for course in courses
    ])


# Get Course by ID
@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):

    conn = get_connection()

    course = conn.execute(
        "SELECT * FROM courses WHERE id=?",
        (course_id,)
    ).fetchone()

    conn.close()

    if course is None:

        return jsonify({
            "message": "Course not found"
        }), 404

    return jsonify(dict(course))


if __name__ == "__main__":
    app.run(port=5001, debug=True)