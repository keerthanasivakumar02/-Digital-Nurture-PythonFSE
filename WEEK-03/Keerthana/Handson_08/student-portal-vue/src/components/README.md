# Student Portal - Hands-on 08 (Vue.js)

## 📌 Objective

This hands-on demonstrates the development of a **Student Portal** using **Vue.js 3** with the **Composition API**, **Vue Router**, and **Pinia**. The project focuses on creating reusable components, implementing client-side routing, managing reactive state, and sharing application data using Pinia.

---

## 🛠️ Technologies Used

- Vue.js 3
- Vite
- Composition API
- Vue Router
- Pinia
- HTML5
- CSS3
- JavaScript (ES6)

---

## 📂 Project Structure

```
student-portal-vue
│
├── src
│   ├── components
│   │   ├── Header.vue
│   │   └── CourseCard.vue
│   │
│   ├── views
│   │   ├── HomeView.vue
│   │   ├── CoursesView.vue
│   │   ├── CourseDetailView.vue
│   │   └── ProfileView.vue
│   │
│   ├── router
│   │   └── index.js
│   │
│   ├── stores
│   │   └── enrollment.js
│   │
│   ├── App.vue
│   └── main.js
│
├── package.json
└── README.md
```

---

# Task 1 – Vue Components & Reactive Data

## Features Implemented

- Created reusable Vue components.
- Used Composition API with `<script setup>`.
- Passed data using `defineProps()`.
- Created reactive variables using `ref()`.
- Rendered course cards using `v-for`.
- Implemented real-time course search using `v-model`.
- Used `computed()` to filter courses.

### Concepts Covered

- Single File Components (SFC)
- `ref()`
- `computed()`
- `onMounted()`
- `defineProps()`
- `v-for`
- `v-model`

---

# Task 2 – Vue Router

## Features Implemented

Configured routing between multiple pages.

### Routes

| Route | Component |
|--------|-----------|
| / | HomeView |
| /courses | CoursesView |
| /courses/:id | CourseDetailView |
| /profile | ProfileView |

### Router Features

- Navigation using `<RouterLink>`
- Page rendering using `<RouterView>`
- Dynamic routing using `useRoute()`
- Programmatic navigation using `useRouter().push()`
- Navigation guard using `router.beforeEach()`

---

# Task 3 – Pinia State Management

## Features Implemented

Created a centralized Pinia store for managing enrolled courses.

### Store

- enrolledCourses
- totalCredits
- enroll(course)
- unenroll(courseId)

### Pinia Features

- Shared application state
- Reactive updates
- Automatic UI synchronization
- Total credits calculation
- Remove enrolled courses

---

## Application Workflow

1. Open the Home page.
2. Navigate to Courses.
3. Search courses using the search bar.
4. Click **Enroll** to enroll in a course.
5. Navigate to Profile.
6. View enrolled courses.
7. Remove courses if required.
8. Observe state updates in Vue DevTools.

---

## Learning Outcomes

Successfully learned:

- Vue.js 3 Composition API
- Reactive state using `ref()`
- Computed properties
- Component communication
- Props
- Event emission (`$emit`)
- Vue Router
- Dynamic routing
- Navigation Guards
- Pinia Store
- Shared State Management
- Vue DevTools

---

## Expected Output

- Home page with navigation.
- Course listing page.
- Search functionality.
- Course detail page.
- Profile page displaying enrolled courses.
- Header displaying enrolled course count.
- Total credits calculation.
- State updates visible in Vue DevTools.

---

## Conclusion

Successfully developed a **Student Portal** using **Vue.js 3**, implementing reusable components, reactive state management, client-side routing, and centralized application state using Pinia. The project demonstrates modern Vue development practices and provides hands-on experience with Composition API, Vue Router, and Pinia.