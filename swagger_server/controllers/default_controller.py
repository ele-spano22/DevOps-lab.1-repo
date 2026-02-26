import connexion
from swagger_server.models.student import Student
from swagger_server.service.student_service import *

def add_student(body):  # noqa: E501
    """Add a new student

    Adds a student to the system # noqa: E501

    :param body: Student object to add
    :type body: dict | bytes

    :rtype: int
    """
    if connexion.request.is_json:
        body = Student.from_dict(connexion.request.get_json())
        return add(body)
    return 500, 'error'


def delete_student(student_id):  # noqa: E501
    """Delete a student

    Delete a single student # noqa: E501

    :param student_id: The student ID
    :type student_id: int

    :rtype: None
    """
    return delete(student_id)


def get_student_by_id(student_id):  # noqa: E501
    """Get a student

    Returns a single student # noqa: E501

    :param student_id: The student ID
    :type student_id: int

    :rtype: Student
    """
    return get_by_id(student_id)
