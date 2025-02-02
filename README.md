# User Authentication and Dashboard System

This project is a Flask-based web application that provides user authentication using JWT and role-based dashboards for Schools, Parents, and Students. The system includes a database with tables for Users, Students, and Student Achievements.

## Features

- User authentication with JWT
- Role-based access to dashboards
- SQLite database integration
- Flask API endpoints for login and dashboard access
- Secure password handling (currently in plain text, should use hashing)

## Technologies Used

- Python (Flask, Flask-SQLAlchemy, Flask-JWT-Extended)
- SQLite database
- HTML templates for dashboards

## Installation

### Prerequisites

- Python 3.x installed
- Virtual environment (recommended)

### Steps to Run the Application

1. Clone this repository:

    ```sh
    git clone https://github.com/hikma0803/Slate-Backend-Developer-Assignment_Task
   
    ```

    **Error Handling:**  
    - If the `git clone` command fails, ensure that you have Git installed and use a valid repository URL.

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

    **Error Handling:**  
    - If the virtual environment creation fails, ensure that Python 3.x is installed.
    - On Windows, you might need to use `python3` instead of `python`.

3. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

    **Error Handling:**  
    - If this command fails, make sure you have `pip` installed and that `requirements.txt` is in the project directory.
    - Use `pip install --upgrade pip` to update `pip`.

4. Run the application:

    ```sh
    python app.py
    ```

    **Error Handling:**  
    - If this command doesn't work, check that you are in the correct directory where `app.py` is located.
    - If you get a "ModuleNotFoundError," make sure you have installed all the dependencies.

5. Access the application in a browser at `http://127.0.0.1:5000/`

## API Endpoints

### Authentication

- **POST /auth/login**
  - Request body (JSON):
  
    ```json
    {
      "email": "user@example.com",
      "password": "password123",
      "role": "Student"
    }
    ```

  - Response (on success):
  
    ```json
    {
      "message": "Login successful",
      "token": "<jwt-token>",
      "dashboard_url": "/dashboard/student"
    }
    ```

### Dashboard Access (JWT Required)

- **GET /dashboard**
  - Requires JWT token in the request header.
  - Returns the corresponding dashboard template based on the user's role.

## Database Models

### User Table

- `id`: Integer (Primary Key)
- `name`: String
- `email`: String (Unique, Required)
- `password`: String (Required, should be hashed)
- `role`: String ('School', 'Parent', 'Student')
- `linked_student_id`: Integer (Foreign Key to Student)

### Student Table

- `id`: Integer (Primary Key)
- `name`: String (Required)
- `school_name`: String (Required)
- `achievements`: Relationship to `StudentAchievement`

### StudentAchievement Table

- `id`: Integer (Primary Key)
- `student_id`: Integer (Foreign Key to Student, Required)
- `achievement`: String (Required)

## Future Improvements

- Secure password storage using hashing (e.g., Flask-Bcrypt)
- Implement user registration endpoint
- Improve UI with Bootstrap
- Expand API functionality for student and parent interactions
