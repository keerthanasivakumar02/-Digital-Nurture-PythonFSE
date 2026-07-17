import { useState, useEffect } from "react";


import Header from "./components/Header";
import Footer from "./components/Footer";
import CourseCard from "./components/CourseCard";
import StudentProfile from "./components/StudentProfile";

function App() {

  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState("");
  const [enrolledCourses, setEnrolledCourses] = useState([]);
  const [error, setError] = useState("");
  useEffect(() => {

  fetch("https://jsonplaceholder.typicode.com/posts")

    .then((response) => {

      if (!response.ok) {
        throw new Error("Unable to fetch courses.");
      }

      return response.json();

    })

    .then((data) => {

      const courseList = data.slice(0, 5).map((post) => ({
        id: post.id,
        name: post.title,
        code: `CS10${post.id}`,
        credits: 3,
        grade: "A",
      }));

      setCourses(courseList);

      setLoading(false);

    })

    .catch((err) => {

      setError(err.message);

      setLoading(false);

    });

}, []);
// This useEffect runs only when the 'courses' state changes.
// The dependency array [courses] prevents it from running after every render.
useEffect(() => {

  console.log("Courses updated");

}, [courses]);

  const filteredCourses = courses.filter((course) =>
    course.name.toLowerCase().includes(searchTerm.toLowerCase())
  );
  
const handleEnroll = (course) => {

  setEnrolledCourses((prev) => [...prev, course]);

};

  return (
    <>
      <Header
      siteName="Student Portal"
      enrolledCount={enrolledCourses.length}
      />

      <main>

        <h2>Welcome to the Student Portal</h2>

        <p>Manage your courses, profile and grades.</p>

        <input
        type="text"
        placeholder="Search Courses..."
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        />
        {loading && <p>Loading...</p>}
        {error && <p>{error}</p>}

        {!loading &&
        filteredCourses.map(course => (
          <CourseCard
          key={course.id}
          {...course}
          onEnroll={handleEnroll}
          />
          ))}

      </main>
      <StudentProfile />

      <Footer />
    </>
  );
}

export default App;

// []  -> Runs only once after the component mounts.
// [courses] -> Runs whenever the courses state changes.
// No dependency array -> Runs after every render.