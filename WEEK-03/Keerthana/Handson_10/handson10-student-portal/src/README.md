# HANDS-ON 10: API Integration & Advanced State Management

## Digital Nurture 5.0 - Module 2: Frontend Development

---

# Project Title

**Student Portal – API Integration & Advanced State Management**

---

# Overview

This hands-on demonstrates how to build a scalable React application using a centralized API service layer and Redux Toolkit for state management. The application uses Axios interceptors, async thunks, selectors, and global error handling to improve maintainability and user experience.

---

# Objectives

- Build a centralized API service layer using Axios.
- Configure request and response interceptors.
- Implement Redux Toolkit with `createAsyncThunk`.
- Manage loading, success, and error states.
- Use selectors for accessing Redux state.
- Implement a global Error Boundary.
- Understand NgRx (Angular) and Pinia (Vue) state management concepts.
- Compare state management approaches across React, Angular, and Vue.

---

# Technologies Used

- React
- Vite
- Axios
- Redux Toolkit
- React Redux
- JavaScript (ES6)

---

# Project Structure

```text
handson10-student-portal/
│
├── src/
│   ├── api/
│   │   ├── apiClient.js
│   │   └── courseApi.js
│   │
│   ├── components/
│   │   └── ErrorBoundary.jsx
│   │
│   ├── redux/
│   │   ├── store.js
│   │   ├── courseSlice.js
│   │   └── selectors.js
│   │
│   ├── App.jsx
│   ├── main.jsx
│   └── index.css
│
├── package.json
└── README.md
```

---

# Task 1: Build a Centralized API Service Layer

## Features Implemented

- Created a reusable Axios instance (`apiClient.js`).
- Configured a common `baseURL`.
- Added default request headers.
- Configured a request timeout.
- Added a request interceptor to attach a mock Authorization token.
- Added a response interceptor to return only `response.data`.
- Standardized API error handling.
- Created reusable API functions:
  - `getAllCourses()`
  - `getCourseById(id)`
  - `enrollStudent(studentId, courseId)`

### Benefits

- Single location for API configuration.
- Easy to switch API environments.
- Consistent error handling.
- Cleaner React components.

---

# Task 2: Advanced Redux Toolkit – Async Thunks

## Features Implemented

- Configured Redux store using `configureStore`.
- Created `courseSlice`.
- Implemented `createAsyncThunk()` for asynchronous API calls.
- Managed asynchronous states:
  - Pending
  - Fulfilled
  - Rejected
- Added Redux selectors:
  - `selectCourses`
  - `selectCoursesLoading`
  - `selectCoursesError`
- Components access Redux data through selectors.

## Redux Data Flow

```text
Component
      ↓
Dispatch Async Thunk
      ↓
API Service
      ↓
Axios Client
      ↓
Server
      ↓
Redux Store
      ↓
Selectors
      ↓
Component
```

---

# Task 3: Global Error Handling

## React Error Boundary

Implemented a global Error Boundary that:

- Catches rendering errors.
- Logs errors to the console.
- Displays a fallback UI instead of crashing the application.

---

# Angular NgRx Concept

NgRx follows a Redux-based architecture.

```text
Component
      ↓
Dispatch Action
      ↓
Effect
      ↓
API Call
      ↓
Reducer
      ↓
Store
      ↓
Selector
      ↓
Component
```

**Key Components:**

- Actions
- Reducers
- Effects
- Store
- Selectors

---

# Vue Pinia Concept

Pinia provides a simpler state management solution with:

- Async actions
- `$reset()` for resetting store state
- `storeToRefs()` for maintaining reactivity

---

# Framework Comparison

| Feature | React + Redux Toolkit | Angular + NgRx | Vue + Pinia |
|---------|------------------------|----------------|-------------|
| State Management | Redux Store | NgRx Store | Pinia Store |
| Async API Calls | createAsyncThunk | Effects | Async Actions |
| Selectors | Yes | Yes | storeToRefs |
| Boilerplate | Medium | High | Low |
| Learning Curve | Medium | High | Easy |
| Error Handling | Error Boundary | ErrorHandler Service | app.config.errorHandler |

---

# Learning Outcomes

After completing this hands-on, I learned:

- How to build a centralized API layer using Axios.
- How Axios request and response interceptors work.
- How Redux Toolkit manages application state.
- How `createAsyncThunk` simplifies asynchronous API calls.
- How selectors improve maintainability.
- How Error Boundaries prevent application crashes.
- The differences between Redux Toolkit, NgRx, and Pinia.

---

# Conclusion

This hands-on demonstrates modern frontend development practices by implementing a centralized API layer, Redux Toolkit state management, asynchronous API handling, selectors, and global error handling. These techniques improve application scalability, maintainability, and reliability while providing a better user experience. It also provides an overview of state management approaches in React, Angular, and Vue.