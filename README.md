# FastAPI Student Management API

This is a simple REST API built using **FastAPI** and **MongoDB** to manage student records. 

## Features
- Create a new student record
- Retrieve student details
- Update existing student information
- Delete a student record

## Tech Stack
- **Framework:** FastAPI
- **Database:** MongoDB
- **Database Driver:** PyMongo
- **Server:** Uvicorn
- **Language:** Python 3.x

## Prerequisites
- Python 3.8 or higher installed on your system.
- MongoDB running locally on `mongodb://localhost:27017/` (or a MongoDB Atlas connection string).

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/sandeshsachan054-tech/fastapi-student-api.git](https://github.com/sandeshsachan054-tech/fastapi-student-api.git)
   cd fastapi-student-api

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # For Windows:
   venv\Scripts\activate
   # For macOS/Linux:
   source venv/bin/activate

3. Install the required dependencies:
   ```bash
    pip install fastapi uvicorn pymongo python-dotenv

4. Running MongoDB via Terminal
a. if your MongoDB is not running in the background, you can start manually from terminal
   ```bash
   mongod

b. To interact with your database, Open a new terminal window and run
   ```bash
   mongosh
   
5. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload

Usage:

​Once the server is running, you can interact with the API using FastAPI's built-in Swagger UI.

​a. Swagger UI: Open http://127.0.0.1:8000/docs in your browser to test the API endpoints directly.

​b. Alternative (ReDoc): Open http://127.0.0.1:8000/redoc for standard API documentation.

​Example Request (Create Student):
​POST /students

json
{
  "name": "ABC"
  "age": 5,
  "course": "B.Tech"
}
