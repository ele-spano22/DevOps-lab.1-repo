import os
import tempfile
from functools import reduce
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import abort


db_dir_path = tempfile.gettempdir()
db_file_path = os.path.join(db_dir_path, "students.json")
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongodb:27017/")
client = MongoClient(MONGO_URI)
db = client["student_db"]
collection = db["students"]

def add(student):
    student_dict = student.to_dict()
    student_dict.pop("student_id", None)

    result = collection.insert_one(student_dict)

    student_dict["student_id"] = str(result.inserted_id)
    return student_dict, 201


def get_by_id(student_id):
    student = collection.find_one({"_id": ObjectId(student_id)})

    if not student:
        abort(404, "Student not found")

    student["student_id"] = str(student["_id"])
    del student["_id"]

    return student


def delete(student_id):
    result = collection.delete_one({"_id": ObjectId(student_id)})

    if result.deleted_count == 0:
        abort(404, "Student not found")

    return {}, 200