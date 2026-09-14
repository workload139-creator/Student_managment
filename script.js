

function validateForm() {

    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let course = document.getElementById("course").value.trim();
    let marks = document.getElementById("marks").value.trim();

    let message = document.getElementById("message");


    if (name === "") {

        message.innerText = "Please enter name.";

        return false;
    }


    if (email === "") {

        message.innerText = "Please enter email.";

        return false;
    }


    if (course === "") {

        message.innerText = "Please enter course.";

        return false;
    }


    if (marks === "") {

        message.innerText = "Please enter marks.";

        return false;
    }


    return true;
}


function searchStudents() {

    let input =
        document.getElementById("search")
        .value
        .toLowerCase();

    let rows =
        document
        .getElementById("studentTable")
        .getElementsByTagName("tr");


    for (let i = 1; i < rows.length; i++) {

        let text =
            rows[i].innerText.toLowerCase();

        if (text.includes(input)) {

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