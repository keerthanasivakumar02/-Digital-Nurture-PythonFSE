# Student Portal – Hands-on 6

## React Routing & State Management

This project is developed as part of the Digital Nurture 5.0 Frontend Development training.

## Topics Covered

- React Router v6
- BrowserRouter
- Routes and Route
- Link
- useNavigate
- useParams
- Context API
- useContext
- createContext
- Redux Toolkit
- configureStore
- createSlice
- Provider
- useDispatch
- useSelector

---

## Project Setup

### Install Dependencies

```bash
npm install
```

### Install React Router

```bash
npm install react-router-dom
```

### Install Redux Toolkit

```bash
npm install @reduxjs/toolkit react-redux
```

### Run the Project

```bash
npm run dev
```

Open the application in your browser:

```
http://localhost:5173
```

---

## Project Structure

```
student-portal-routing
│
├── src
│   ├── components
│   │   ├── Header.jsx
│   │   └── Footer.jsx
│   │
│   ├── pages
│   │   ├── HomePage.jsx
│   │   ├── CoursesPage.jsx
│   │   ├── CourseDetailPage.jsx
│   │   └── ProfilePage.jsx
│   │
│   ├── context
│   │   └── EnrollmentContext.jsx
│   │
│   ├── redux
│   │   ├── store.js
│   │   └── enrollmentSlice.js
│   │
│   ├── data.js
│   ├── App.jsx
│   ├── main.jsx
│   └── index.css
│
├── package.json
└── README.md
```

---

# Task 1 – React Router

Implemented:

- BrowserRouter
- Routes
- Route
- Home Page
- Courses Page
- Profile Page
- Course Detail Page
- Navigation using Link
- Dynamic routing using useParams
- Programmatic navigation using useNavigate

Routes:

```
/
```

Home Page

```
/courses
```

Courses Page

```
/courses/:courseId
```

Course Details

```
/profile
```

Profile Page

---

# Task 2 – Context API

Implemented:

- createContext()
- EnrollmentProvider
- useContext()
- Global enrolled courses state
- Enroll functionality
- Remove functionality

Features:

- Shared enrollment state
- Header displays enrolled count
- Profile page displays enrolled courses
- Remove course from enrollment

---

# Task 3 – Redux Toolkit

Implemented:

- configureStore()
- createSlice()
- Provider
- useDispatch()
- useSelector()

Reducers:

- enroll()
- unenroll()

State:

```javascript
{
    enrolledCourses: []
}
```

Actions:

- enrollment/enroll
- enrollment/unenroll

---

## Features

- Multi-page navigation
- Dynamic route parameters
- Programmatic navigation
- Global state using Context API
- Global state using Redux Toolkit
- Course enrollment
- Remove enrolled course
- Shared application state
- Redux DevTools support

---

## Expected Output

- Home page loads successfully.
- Navigation works without page reload.
- Course details open using dynamic URLs.
- Enrolling redirects to Profile page.
- Enrolled course count updates automatically.
- Profile displays enrolled courses.
- Remove button removes enrolled courses.
- Redux DevTools displays enroll and unenroll actions.
- Redux state updates correctly across all components.

---

## Technologies Used

- React
- Vite
- React Router DOM
- Context API
- Redux Toolkit
- React Redux
- JavaScript (ES6+)
- JSX

---

## Learning Outcomes

After completing this hands-on, the following concepts were learned:

- React Router setup
- Client-side routing
- Dynamic routes
- Route parameters
- Navigation using hooks
- Context API
- Global state management
- Redux Toolkit
- Redux Store
- Redux Slice
- Dispatching actions
- Reading Redux state using useSelector
- Debugging state using Redux DevTools

---

## Author

**Keerthana Sivakumar**

Digital Nurture 5.0 – Frontend Development

Hands-on 6 – React Routing & State Management