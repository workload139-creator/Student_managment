function validateForm() {

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const course = document.getElementById("course").value.trim();
    const marks = document.getElementById("marks").value.trim();

    const message = document.getElementById("message");

    if (name === "" || email === "" || course === "" || marks === "") {

        message.textContent = "Please fill all fields.";

        return false;
    }

    if (marks < 0 || marks > 100) {

        message.textContent = "Marks must be between 0 and 100.";

        return false;
    }

    return true;
}


function searchStudents() {

    const input = document.getElementById("search");

    const filter = input.value.toLowerCase();

    const table = document.getElementById("studentTable");

    if (!table) {
        return;
    }

    const rows = table
        .getElementsByTagName("tbody")[0]
        .getElementsByTagName("tr");


    for (let i = 0; i < rows.length; i++) {

        const text = rows[i].textContent.toLowerCase();

        if (text.includes(filter)) {

            rows[i].style.display = "";

        } else {

            rows[i].style.display = "none";
        }
    }
}


function confirmDelete() {

    return confirm(
        "Are you sure you want to delete this student?"
    );
}
