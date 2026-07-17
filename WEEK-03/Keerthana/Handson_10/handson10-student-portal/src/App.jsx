import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";

import { fetchAllCourses } from "./redux/courseSlice";
import {
  selectCourses,
  selectCoursesLoading,
  selectCoursesError,
} from "./redux/selectors";

function App() {  
  const dispatch = useDispatch();

  const courses = useSelector(selectCourses);
  const loading = useSelector(selectCoursesLoading);
  const error = useSelector(selectCoursesError);

  useEffect(() => {
    dispatch(fetchAllCourses());
  }, [dispatch]);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Student Portal</h1>

      {loading && <h2>Loading...</h2>}

      {error && <h2>Error: {error}</h2>}

      {!loading &&
        !error &&
        courses.map((course) => (
          <div
            key={course.id}
            style={{
              border: "1px solid gray",
              marginBottom: "10px",
              padding: "10px",
              borderRadius: "5px",
            }}
          >
            <h3>{course.title}</h3>
            <p>{course.body}</p>
          </div>
        ))}
    </div>
  );
}

export default App;