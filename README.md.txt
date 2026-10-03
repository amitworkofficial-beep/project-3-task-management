# Task Management System

## Project 3 - Practical Implementation Project

The Task Management System is a full-stack web application developed using Python Flask, SQLite, HTML, CSS, and JavaScript.

## Features

- Add new tasks
- View all tasks
- Mark tasks as completed
- Delete tasks
- Store task information in SQLite database
- Form validation
- Responsive user interface
- Database integration

## Technologies Used

- Python
- Flask
- SQLite
- HTML5
- CSS3
- JavaScript
- Jinja2

## Project Structure

project-3-task-management/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── tasks.db
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js

## How to Run

1. Install Python.
2. Install Flask:

   pip install -r requirements.txt

3. Run the application:

   python app.py

4. Open the following address in a web browser:

   http://127.0.0.1:5000

## Database

The application uses SQLite to store task records.

Each task contains:

- ID
- Title
- Description
- Status

## Testing

The application was tested by:

- Adding a new task
- Displaying the task
- Marking a task as completed
- Deleting a task
- Checking the empty task state
- Testing required form input
- Restarting the Flask application

## Conclusion

This project demonstrates the practical implementation of full-stack development concepts including frontend design, backend development, database integration, routing, form handling, CRUD operations, validation, and application testing.