import connexion
from swagger_server.models.student import Student
from swagger_server.service import student_service


def add_student(body):  # noqa: E501
    """Add a new student

    Adds a student to the system
    """

    if connexion.request.is_json:
        body = Student.from_dict(connexion.request.get_json())
        return student_service.add(body)

    return 500, "error"


def delete_student(student_id):  # noqa: E501
    """Delete a student"""

    return student_service.delete(student_id)


def get_student_by_id(student_id):  # noqa: E501
    """Get a student"""

    return student_service.get_by_id(student_id)


def get_average_grade(student_id):
    """Get the average grade of a student"""

    return student_service.get_average_grade(student_id)