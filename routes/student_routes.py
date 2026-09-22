from typing import List

from fastapi import APIRouter, Query, Path, status

from models.student_model import Student
from controllers import student_controller


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


# =====================================================
# CREATE ONE
# =====================================================

@router.post(
    "",
    status_code=status.HTTP_201_CREATED
)
def create_student(
    student: Student
):

    return student_controller.create_student(
        student
    )


# =====================================================
# CREATE MULTIPLE
# =====================================================

@router.post(
    "/bulk",
    status_code=status.HTTP_201_CREATED
)
def create_multiple_students(
    students: List[Student]
):

    return student_controller.create_multiple_students(
        students
    )


# =====================================================
# GET ALL
# =====================================================

@router.get("")
def get_all_students(
    limit: int = Query(
        10,
        ge=1,
        le=100
    )
):

    return student_controller.get_all_students(
        limit
    )


# =====================================================
# SEARCH BY ID
# =====================================================

@router.get("/search")
def search_student(
    student_id: str = Query(...)
):

    return student_controller.get_student_by_id(
        student_id
    )


# =====================================================
# GET ONE BY ID
# =====================================================

@router.get("/{student_id}")
def get_student(
    student_id: str = Path(...)
):

    return student_controller.get_student_by_id(
        student_id
    )


# =====================================================
# UPDATE
# =====================================================

@router.put("/{student_id}")
def update_student(
    student_id: str,
    student: Student
):

    return student_controller.update_student(
        student_id,
        student
    )


# =====================================================
# DELETE
# =====================================================

@router.delete("/{student_id}")
def delete_student(
    student_id: str
):

    return student_controller.delete_student(
        student_id
    )