# FastAPI Student Management API

A REST API built using **FastAPI** and **MongoDB** to manage student records with CRUD operations, validation, and student search by ID.

## Features

- Create a student
- Create multiple students
- Get all students
- Search student by ID
- Update student
- Delete student
- Input validation
- MongoDB ObjectId validation

## Tech Stack

- Framework: FastAPI
- Database:  MongoDB
- Driver:    PyMongo
- Server:    Uvicorn
- Language:  Python 3.x ( required python3.8+ version)

## Project Structure

```text
fastapi-student-api/
├── main.py
├── database.py
├── controllers/
│   └── student_controller.py
├── models/
│   └── student_model.py
├── services/
│   └── student_service.py
├── repositories/
│   └── student_repository.py
└── routes/
    └── student_routes.py
```


## Installation & Setup

1. Clone Repository-
   ```bash
   git clone https://github.com/sandeshsachan054-tech/fastapi-student-api.git
   cd fastapi-student-api
   ```

2. Create Virtual Environment-

   ```bash
   python -m venv venv
   ```
for windows-

   ```bash
    venv\Scripts\activate
   ```

3. Install Dependencies:
   ```bash
   pip install fastapi uvicorn pymongo python-dotenv
   ```

4. Start MongoDB
   ```bash
   mongod
   ```

5. Run API
   ```bash
   uvicorn main:app --reload
   ```

## API Documentation

Swagger UI:
http://127.0.0.1:8000/docs

ReDoc:
http://127.0.0.1:8000/redoc

Click an endpoint and select:
Try it out

## Swagger will display:
-Request URL
-Request body
-HTTP status code
-Response body
-Response headers


## API Endpoints:

| Method | Endpoint                 | Description              |
| ------ | ------------------------ | ------------------------ |
| POST   | `/students`              | Create student           |
| POST   | `/students/bulk`         | Create multiple students |
| GET    | `/students`              | Get all students         |
| GET    | `/students/search`       | Search student by ID     |
| GET    | `/students/{student_id}` | Get student by ID        |
| PUT    | `/students/{student_id}` | Update student           |
| DELETE | `/students/{student_id}` | Delete student           |


## Request Flow Example:
When a client creates a student:

Client
  │
  │ POST /students
  ▼
Route
  │
  ▼
Controller
  │
  ▼
Service
  │
  ▼
Repository
  │
  ▼
MongoDB
  │
  ▼
Repository Result
  │
  ▼
Service
  │
  ▼
Controller
  │
  ▼
JSON Response


## Github:
https://github.com/sandeshsachan054-tech