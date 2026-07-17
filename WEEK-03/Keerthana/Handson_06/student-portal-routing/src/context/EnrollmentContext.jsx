import { createContext, useState } from "react";

// Create Context
export const EnrollmentContext = createContext();

// Provider Component
export function EnrollmentProvider({ children }) {

  const [enrolledCourses, setEnrolledCourses] = useState([]);

  // Enroll Course
  const enrollCourse = (course) => {
    setEnrolledCourses((prev) => [...prev, course]);
  };

  // Remove Course
  const removeCourse = (id) => {
    setEnrolledCourses((prev) =>
      prev.filter((course) => course.id !== id)
    );
  };

  return (
    <EnrollmentContext.Provider
      value={{
        enrolledCourses,
        enrollCourse,
        removeCourse,
      }}
    >
      {children}
    </EnrollmentContext.Provider>
  );
}