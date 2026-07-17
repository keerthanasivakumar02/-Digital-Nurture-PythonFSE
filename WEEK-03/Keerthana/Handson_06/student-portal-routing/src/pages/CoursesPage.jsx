import { Link, useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import { enroll } from "../redux/enrollmentSlice";
import { courses } from "../data";

function CoursesPage() {

  const dispatch = useDispatch();

  const navigate = useNavigate();

  function handleEnroll(course) {

    dispatch(enroll(course));

    navigate("/profile");

  }

  return (

    <div>

      <h2>Courses</h2>

      {courses.map((course) => (

        <div
          key={course.id}
          className="course-card"
        >

          <h3>{course.name}</h3>

          <p>{course.code}</p>

          <Link to={`/courses/${course.id}`}>
            View Details
          </Link>

          {" "}

          <button
            onClick={() => handleEnroll(course)}
          >
            Enroll
          </button>

        </div>

      ))}

    </div>

  );

}

export default CoursesPage;