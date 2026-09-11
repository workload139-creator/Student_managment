from flask import Flask, render_template, request, redirect, jsonify
import sqlite3
import os

BASE_DIR = "/storage/emulated/0"
DB_PATH = os.path.join(BASE_DIR, "soos.db")

app = Flask(
    __name__,
    template_folder=BASE_DIR,
    static_folder=BASE_DIR,
    static_url_path="/files"
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
    return render_template("index.html")


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

    return redirect("/students")


@app.route("/students")
def students():

    conn = get_db()

    data = conn.execute(
        "SELECT * FROM students ORDER BY id DESC"
    ).fetchall()

    conn.close()

    return render_template(
        "index.html",
        students=data
    )


@app.route("/delete/<int:student_id>")
def delete_student(student_id):

    conn = get_db()

    conn.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()
    conn.close()

    return redirect("/students")


if __name__ == "__main__":

    create_table()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )