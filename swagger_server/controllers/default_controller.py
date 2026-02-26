import connexion
import six

from swagger_server.models.student import Student  # noqa: E501
from swagger_server import util


def add_student(body):  # noqa: E501
    """Add a new student

    Adds a student to the system # noqa: E501

    :param body: Student object to add
    :type body: dict | bytes

    :rtype: int
    """
    if connexion.request.is_json:
        body = Student.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_student(student_id):  # noqa: E501
    """Delete a student

    Delete a single student # noqa: E501

    :param student_id: The student ID
    :type student_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_student_by_id(student_id):  # noqa: E501
    """Get a student

    Returns a single student # noqa: E501

    :param student_id: The student ID
    :type student_id: int

    :rtype: Student
    """
    return 'do some magic!'
