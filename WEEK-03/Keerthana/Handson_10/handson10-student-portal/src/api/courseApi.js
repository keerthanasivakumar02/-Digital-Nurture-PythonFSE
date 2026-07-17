import apiClient from "./apiClient";

// Get all courses
export const getAllCourses = () => {
  return apiClient.get("/posts");
};

// Get course by ID
export const getCourseById = (id) => {
  return apiClient.get(`/posts/${id}`);
};

// Enroll student (Mock API)
export const enrollStudent = (studentId, courseId) => {
  return apiClient.post("/posts", {
    studentId,
    courseId,
  });
};