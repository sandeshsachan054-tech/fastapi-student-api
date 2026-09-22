from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from routes.student_routes import router as student_router
from errors.validation import validation_exception_handler


app = FastAPI(
    title="Student Management API",
    description="Student CRUD API",
    version="1.0.0"
)


# Validation Error Handler

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)


# Student Routes

app.include_router(
    student_router
)


@app.get("/")
def home():

    return {
        "success": True,
        "message": "Student Management API is running"
    }