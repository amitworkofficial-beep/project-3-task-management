from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = "tasks.db"


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT NOT NULL DEFAULT 'Pending'
        )
    """)

    connection.commit()
    connection.close()


@app.route("/")
def index():
    connection = get_db_connection()
    tasks = connection.execute(
        "SELECT * FROM tasks ORDER BY id DESC"
    ).fetchall()
    connection.close()

    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form["title"]
    description = request.form["description"]

    connection = get_db_connection()

    connection.execute(
        """
        INSERT INTO tasks (title, description)
        VALUES (?, ?)
        """,
        (title, description)
    )

    connection.commit()
    connection.close()

    return redirect(url_for("index"))


@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    connection = get_db_connection()

    connection.execute(
        "UPDATE tasks SET status = 'Completed' WHERE id = ?",
        (task_id,)
    )

    connection.commit()
    connection.close()

    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    connection = get_db_connection()

    connection.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()
    connection.close()

    return redirect(url_for("index"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)