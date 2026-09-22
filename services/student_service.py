from bson import ObjectId
from fastapi import HTTPException, status

from repositories import student_repository


# =====================================================
# CREATE ONE STUDENT
# =====================================================

def create_student(student_data: dict):

    result = student_repository.create_student(
        student_data
    )

    return {
        "id": str(result.inserted_id),
        "name": student_data["name"],
        "age": student_data["age"],
        "course": student_data["course"]
    }
# =====================================================
# CREATE MULTIPLE STUDENTS
# =====================================================

def create_multiple_students(
    students_data: list
):

    result = student_repository.create_multiple_students(
        students_data
    )

    return {
        "inserted_ids": [
            str(student_id)
            for student_id in result.inserted_ids
        ]
    }


# =====================================================
# GET ALL STUDENTS
# =====================================================

def get_all_students(limit: int):

    students = student_repository.get_all_students(
        limit
    )

    for student in students:
        student["_id"] = str(student["_id"])

    return students


# =====================================================
# GET STUDENT BY ID
# =====================================================

def get_student_by_id(student_id: str):

    # Check ObjectId
    if not ObjectId.is_valid(student_id):

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "field": "student_id",
                "message": "Invalid student ID",
                "reason": (
                    "Student ID valid MongoDB "
                    "ObjectId nahi hai"
                ),
                "input": student_id
            }
        )

    student = student_repository.get_student_by_id(
        student_id
    )

    # Student not found
    if student is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "field": "student_id",
                "message": "Student not found",
                "reason": (
                    "Is ID ke saath database "
                    "me student nahi mila"
                ),
                "input": student_id
            }
        )

    student["_id"] = str(student["_id"])

    return student


# =====================================================
# UPDATE STUDENT
# =====================================================

def update_student(
    student_id: str,
    student_data: dict
):

    if not ObjectId.is_valid(student_id):

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid student ID"
        )

    result = student_repository.update_student(
        student_id,
        student_data
    )

    if result.matched_count == 0:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return {
        "_id": student_id,
        **student_data
    }


# =====================================================
# DELETE STUDENT
# =====================================================

def delete_student(student_id: str):

    if not ObjectId.is_valid(student_id):

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid student ID"
        )

    result = student_repository.delete_student(
        student_id
    )

    if result.deleted_count == 0:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return {
        "student_id": student_id
    }