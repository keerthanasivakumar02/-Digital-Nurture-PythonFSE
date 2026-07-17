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


// Initial Render

renderCourses(courses);


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