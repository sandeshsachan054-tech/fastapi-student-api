from database import students_collection
from bson import ObjectId


# =====================================================
# CREATE ONE STUDENT
# =====================================================

def create_student(student_data: dict):

    result = students_collection.insert_one(
        student_data
    )

    return result


# =====================================================
# CREATE MULTIPLE STUDENTS
# =====================================================

def create_multiple_students(students_data: list):

    result = students_collection.insert_many(
        students_data
    )

    return result


# =====================================================
# GET ALL STUDENTS
# =====================================================

def get_all_students(limit: int):

    students = list(
        students_collection
        .find()
        .limit(limit)
    )

    return students


# =====================================================
# GET STUDENT BY ID
# =====================================================

def get_student_by_id(student_id: str):

    student = students_collection.find_one(
        {
            "_id": ObjectId(student_id)
        }
    )

    return student


# =====================================================
# UPDATE STUDENT
# =====================================================

def update_student(
    student_id: str,
    student_data: dict
):

    result = students_collection.update_one(
        {
            "_id": ObjectId(student_id)
        },
        {
            "$set": student_data
        }
    )

    return result


# =====================================================
# DELETE STUDENT
# =====================================================

def delete_student(student_id: str):

    result = students_collection.delete_one(
        {
            "_id": ObjectId(student_id)
        }
    )

    return result