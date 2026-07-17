// Import course data
import { courses } from "./data.js";

// ==============================
// TASK 1
// ==============================

// Step 30 - Destructuring
console.log("===== STEP 30 : DESTRUCTURING =====");

courses.forEach(course => {

    const { name, credits } = course;

    console.log(`Course: ${name}, Credits: ${credits}`);

});

// Step 31 - map()
console.log("===== STEP 31 : ARRAY MAP =====");

const formattedCourses = courses.map(course =>
    `${course.code} — ${course.name} (${course.credits} credits)`
);

console.log(formattedCourses);

// Step 32 - filter()
console.log("===== STEP 32 : ARRAY FILTER =====");

const highCreditCourses = courses.filter(course => course.credits >= 4);

console.log(highCreditCourses);

console.log(
    "Number of courses with credits >= 4 :",
    highCreditCourses.length
);

// Step 33 - reduce()
console.log("===== STEP 33 : ARRAY REDUCE =====");

const totalCredits = courses.reduce(

    (total, course) => total + course.credits,

    0

);

console.log("Total Credits Enrolled :", totalCredits);

// Step 34 - Arrow Function
console.log("===== STEP 34 : ARROW FUNCTION =====");

courses.forEach(course => {

    console.log(
        `${course.name} (${course.code}) has ${course.credits} credits and Grade ${course.grade}`
    );

});


// ==============================
// TASK 2 + TASK 3
// ==============================

// Select Elements

const courseGrid = document.querySelector(".course-grid");

const totalCreditsText = document.getElementById("total-credits");

const searchInput = document.getElementById("search-courses");

const sortBtn = document.getElementById("sort-btn");

const selectedCourse = document.getElementById("selected-course");

const loadingMessage = document.getElementById("loading-message");


// Render Function

function renderCourses(courseList) {

    courseGrid.innerHTML = "";

    courseList.forEach(course => {

        const article = document.createElement("article");

        article.className = "course-card";

        article.dataset.id = course.id;

        article.innerHTML = `

            <h3>${course.name}</h3>

            <p><strong>Code:</strong> ${course.code}</p>

            <p><strong>Credits:</strong> ${course.credits}</p>

        `;

        courseGrid.appendChild(article);

    });

}


// Initial Render with Loading State

loadingMessage.style.display = "block";

fetchAllCourses().then(courseList => {

    renderCourses(courseList);

    loadingMessage.style.display = "none";

});


// Total Credits

totalCreditsText.textContent =
`Total Credits Enrolled : ${totalCredits}`;


// ==============================
// STEP 41 - SEARCH
// ==============================

searchInput.addEventListener("input", () => {

    const searchText = searchInput.value.toLowerCase();

    const filteredCourses = courses.filter(course =>

        course.name.toLowerCase().includes(searchText)

    );

    renderCourses(filteredCourses);

});


// ==============================
// STEP 42 - SORT
// ==============================

sortBtn.addEventListener("click", () => {

    const sortedCourses = [...courses];

    sortedCourses.sort(

        (a, b) => b.credits - a.credits

    );

    renderCourses(sortedCourses);

});


// ==============================
// STEP 43 & 44
// EVENT DELEGATION
// ==============================

courseGrid.addEventListener("click", (event) => {

    const card = event.target.closest(".course-card");

    if (!card) return;

    const courseId = Number(card.dataset.id);

    const course = courses.find(c => c.id === courseId);

    selectedCourse.textContent =
        `Selected Course : ${course.name} | Grade : ${course.grade}`;

});

// ======================================
// HANDS-ON 4
// TASK 1 - STEP 45
// ======================================

function fetchUser(id) {

    return fetch(
        "https://jsonplaceholder.typicode.com/users/" + id
    )

    .then(response => response.json())

    .then(user => {

        console.log("User Name :", user.name);

    });

}
fetchUser(1);
// ======================================
// HANDS-ON 4
// TASK 1 - STEP 46
// ======================================

async function fetchUserAsync(id) {

    try {

        const response = await fetch(
            "https://jsonplaceholder.typicode.com/users/" + id
        );

        const user = await response.json();

        console.log("User Name (Async):", user.name);

    }

    catch (error) {

        console.log("Error:", error);

    }

}
fetchUserAsync(1);

// ======================================
// HANDS-ON 4
// TASK 1 - STEP 47
// ======================================

async function fetchAllCourses() {

    // Simulate a 1-second delay
    await new Promise(resolve => setTimeout(resolve, 1000));

    return courses;

}
fetchAllCourses().then(courseList => {

    console.log("Courses Loaded:");

    console.log(courseList);

});

// ======================================
// HANDS-ON 4
// TASK 1 - STEP 49
// ======================================

Promise.all([

    fetch("https://jsonplaceholder.typicode.com/users/1")
        .then(response => response.json()),

    fetch("https://jsonplaceholder.typicode.com/users/2")
        .then(response => response.json())

])

.then(users => {

    console.log("Promise.all() Results");

    console.log("User 1 :", users[0].name);

    console.log("User 2 :", users[1].name);

})

.catch(error => {

    console.log("Error :", error);

});

// ======================================
// HANDS-ON 4
// TASK 3 - STEP 58
// ======================================

axios.interceptors.request.use(config => {

    console.log("API call started:", config.url);

    return config;

});

// ======================================
// HANDS-ON 4
// TASK 3 - STEP 56
// ======================================

async function apiFetch(url) {

    try {

        const response = await axios.get(url, {
            params: {
                userId: 1
            }
        });

        return response.data;

    } catch (error) {

        throw new Error("Unable to fetch data.");

    }

}
async function loadNotifications() {

    const loading = document.getElementById("notification-loading");
    const notificationList = document.getElementById("notification-list");

    loading.style.display = "block";

    try {

        const posts = await apiFetch(
    "https://jsonplaceholder.typicode.com/posts"
);

        loading.style.display = "none";

        notificationList.innerHTML = "";

        posts.slice(0, 5).forEach(post => {

            notificationList.innerHTML += `
                <div class="notification-card">
                    <h3>${post.title}</h3>
                    <p>${post.body}</p>
                </div>
            `;

        });

    } catch (error) {

    loading.style.display = "none";

    notificationList.innerHTML = `
        <div class="error-message">
            <h3>Unable to load notifications.</h3>
            <p>Please try again later.</p>

            <button id="retry-btn">
                Retry
            </button>
        </div>
    `;

    document
        .getElementById("retry-btn")
        .addEventListener("click", () => {

            loadNotifications();

        });

}
}
loadNotifications();    

// ======================================
// HANDS-ON 4
// TASK 3 - STEP 59
// FETCH vs AXIOS
// ======================================

/*
FETCH vs AXIOS

1. Fetch is built into modern browsers.
   Axios is an external library that must be included.

2. Fetch requires response.json() to parse JSON.
   Axios automatically parses JSON and returns response.data.

3. Fetch does not throw errors for HTTP errors (404, 500).
   Axios automatically throws errors for non-2xx responses.
*/