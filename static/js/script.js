document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector(".task-form form");

    if (form) {
        form.addEventListener("submit", function () {
            const title = document.getElementById("title").value.trim();

            if (title === "") {
                alert("Please enter a task title.");
            }
        });
    }
});