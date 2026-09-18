from fastapi import FastAPI, Query, Path, HTTPException, status
from pydantic import BaseModel, Field
from database import students_collection
from bson import ObjectId
from typing import List

app = FastAPI()


class Student(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=5, le=100)
    course: str = Field(min_length=2, max_length=50)


# CREATE SINGLE STUDENT
@app.post("/students",status_code=status.HTTP_201_CREATED)
def create_student(student: Student):

    result = students_collection.insert_one(student.model_dump())

    return {
        "id": str(result.inserted_id),
        **student.model_dump()
    }

# CREATE MULTIPLE STUDENTS 
@app.post("/students/bulk", status_code=status.HTTP_201_CREATED)
def create_multiple_students(students: List[Student]):
    students_data = [student.model_dump() for student in students]

    result = students_collection.insert_many(students_data)

    return {
        "message": f"Successfully  { len(result.inserted_ids)} students add ho gya!",
        "inserted_ids": [str(doc_id) for doc_id in result.inserted_ids]
    }


# READ ALL STUDENTS
@app.get("/students")
def get_students(
    limit: int = Query(..., ge=1, le=10)
):

    students = list(
        students_collection.find().limit(limit)
    )

    for student in students:
        student["_id"] = str(student["_id"])

    return students


# READ ONE
@app.get("/students/{student_id}")
def get_student(
    student_id: str = Path(...)
):

    if not ObjectId.is_valid(student_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid student ID"
        )

    student = students_collection.find_one(
        {"_id": ObjectId(student_id)}
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student["_id"] = str(student["_id"])

    return student


# UPDATE
@app.put("/students/{student_id}")
def update_student(
    student_id: str = Path(...),
    student: Student = ...
):

    if not ObjectId.is_valid(student_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid student ID"
        )

    result = students_collection.update_one(
        {"_id": ObjectId(student_id)},
        {"$set": student.model_dump()}
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "_id": student_id,
        **student.model_dump()
    }


# DELETE
@app.delete("/students/{student_id}")
def delete_student(
    student_id: str = Path(...)
):

    if not ObjectId.is_valid(student_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid student ID"
        )

    result = students_collection.delete_one(
        {"_id": ObjectId(student_id)}
    )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student deleted"
    }