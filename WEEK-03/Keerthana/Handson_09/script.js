
function enrollCourse(courseName) {

    alert(courseName + " Enrolled!")

}

function handleKey(event, courseName) {

    if (event.key === "Enter") {

        enrollCourse(courseName)

    }

}

const buttons = document.querySelectorAll("button")

buttons.forEach(button => {

    button.addEventListener("click", () => {

        alert("Course Enrolled!")

    })

})

const menuButton = document.getElementById("menuButton")

menuButton.addEventListener("click", () => {

    const expanded =
        menuButton.getAttribute("aria-expanded") === "true"

    menuButton.setAttribute(

        "aria-expanded",

        !expanded

    )

})