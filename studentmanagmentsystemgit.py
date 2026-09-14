from flask import Flask, render_template, request, redirect
import sqlite3
import os


# Project folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Database project folder में बनेगी
DB_PATH = os.path.join(BASE_DIR, "soos.db")


app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():

    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            course TEXT NOT NULL,
            marks INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def home():

    conn = get_db()

    data = conn.execute(
        "SELECT * FROM students ORDER BY id DESC"
    ).fetchall()

    conn.close()

    return render_template(
        "index.html",
        students=data
    )


@app.route("/add", methods=["POST"])
def add_student():

    name = request.form["name"]
    email = request.form["email"]
    course = request.form["course"]
    marks = request.form["marks"]

    conn = get_db()

    conn.execute("""
        INSERT INTO students
        (name, email, course, marks)
        VALUES (?, ?, ?, ?)
    """, (name, email, course, marks))

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/delete/<int:student_id>")
def delete_student(student_id):

    conn = get_db()

    conn.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()
    conn.close()

    return redirect("/")


# Create database/table when Gunicorn starts
create_table()


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
