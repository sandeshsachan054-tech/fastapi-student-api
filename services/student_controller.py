from typing import List

from fastapi import Query, Path

from models.student_model import Student
from services import student_service


# =====================================================
# CREATE ONE STUDENT
# =====================================================

def create_student(student: Student):

    result = student_service.create_student(
        student.model_dump()
    )

    return {
        "success": True,
        "message": "Student created successfully",
        **result
    }


# =====================================================
# CREATE MULTIPLE STUDENTS
# =====================================================

def create_multiple_students(
    students: List[Student]
):

    students_data = [
        student.model_dump()
        for student in students
    ]

    result = student_service.create_multiple_students(
        students_data
    )

    return {
        "success": True,
        "message": (
            f"Successfully "
            f"{len(result['inserted_ids'])} "
            f"students add ho gaye"
        ),
        **result
    }


# =====================================================
# GET ALL STUDENTS
# =====================================================

def get_all_students(
    limit: int
):

    students = student_service.get_all_students(
        limit
    )

    return {
        "success": True,
        "total": len(students),
        "students": students
    }


# =====================================================
# GET STUDENT BY ID
# =====================================================

def get_student_by_id(
    student_id: str
):

    student = student_service.get_student_by_id(
        student_id
    )

    return {
        "success": True,
        "message": "Student found successfully",
        "student": student
    }


# =====================================================
# UPDATE STUDENT
# =====================================================

def update_student(
    student_id: str,
    student: Student
):

    result = student_service.update_student(
        student_id,
        student.model_dump()
    )

    return {
        "success": True,
        "message": "Student updated successfully",
        **result
    }


# =====================================================
# DELETE STUDENT
# =====================================================

def delete_student(
    student_id: str
):

    result = student_service.delete_student(
        student_id
    )

    return {
        "success": True,
        "message": "Student deleted successfully",
        **result
    }