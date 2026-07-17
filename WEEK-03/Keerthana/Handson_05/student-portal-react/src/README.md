# Student Portal - Hands-on 5

## React Fundamentals - Components, Props, State & Hooks

This project is developed as part of **Digital Nurture 5.0 - Module 2: Frontend Development**.

The application rebuilds the Student Portal using **React** and demonstrates the core concepts of React including components, props, state management, hooks, API integration, loading states, and error handling.

---

## Technologies Used

- React
- Vite
- JavaScript (ES6+)
- JSX
- HTML5
- JSONPlaceholder API

---

## Project Structure

```
student-portal-react/
│
├── src/
│   ├── components/
│   │   ├── Header.jsx
│   │   ├── Footer.jsx
│   │   ├── CourseCard.jsx
│   │   └── StudentProfile.jsx
│   │
│   ├── data.js
│   ├── App.jsx
│   ├── main.jsx
│   └── App.css
│
├── package.json
└── README.md
```

---

## Features

### Task 1 - Project Setup & Components

- React project created using Vite
- Header component
- Footer component
- CourseCard reusable component
- Props used to pass data between components

---

### Task 2 - State Management

- useState Hook
- Dynamic course rendering
- Search functionality
- Enroll button
- Enrolled course count displayed in Header
- List rendering using map()

---

### Task 3 - useEffect & API Integration

- Fetch course data using useEffect
- JSONPlaceholder API integration
- Loading state
- Error handling
- Student Profile form with local state
- useEffect dependency array example

---

## API Used

```
https://jsonplaceholder.typicode.com/posts
```

The first five posts are converted into course objects.

---

## Concepts Covered

- JSX
- Functional Components
- Props
- useState
- useEffect
- Event Handling
- Conditional Rendering
- List Rendering
- API Fetching
- Loading State
- Error State
- Component Communication

---

## How to Run

### Install dependencies

```bash
npm install
```

### Start development server

```bash
npm run dev
```

Open the browser:

```
http://localhost:5173
```

---

## Learning Outcomes

After completing this hands-on, I learned:

- Creating reusable React components
- Passing data using props
- Managing application state using useState
- Rendering dynamic lists
- Filtering data with search
- Handling button click events
- Fetching data using useEffect
- Working with REST APIs
- Implementing loading and error states
- Managing local component state

---

## Author

**Keerthana Sivakumar**

Digital Nurture 5.0 - Frontend Development