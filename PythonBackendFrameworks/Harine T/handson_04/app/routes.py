from flask import Blueprint, jsonify
from .utils import request_get_json, make_response_json

courses_bp = Blueprint("courses", __name__)

courses = []


@courses_bp.route("/api/courses", methods=["GET"])
def get_courses():
    return jsonify(courses)


@courses_bp.route("/api/courses", methods=["POST"])
def add_course():

    data = request_get_json()

    required_fields = ["name", "code", "credits"]

    for field in required_fields:
        if field not in data:
            return make_response_json(
                {
                    "status": "error",
                    "message": f"{field} is required"
                },
                400
            )

    courses.append(data)



    return make_response_json(
        {
            "status": "success",
            "data": data
        },
        201
    )

@courses_bp.route("/api/courses/<int:course_id>", methods=["PUT"])
def update_course(course_id):

    if course_id < 0 or course_id >= len(courses):
        return make_response_json(
            {
                "status": "error",
                "message": "Course not found"
            },
            404
        )

    data = request_get_json()

    required_fields = ["name", "code", "credits"]

    for field in required_fields:
        if field not in data:
            return make_response_json(
                {
                    "status": "error",
                    "message": f"{field} is required"
                },
                400
            )

    courses[course_id] = data

    return make_response_json(
        {
            "status": "success",
            "data": data
        },
        200
    )
@courses_bp.route("/api/courses/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):

    if course_id < 0 or course_id >= len(courses):
        return make_response_json(
            {
                "status": "error",
                "message": "Course not found"
            },
            404
        )

    deleted_course = courses.pop(course_id)

    return make_response_json(
        {
            "status": "success",
            "data": deleted_course
        },
        200
    )