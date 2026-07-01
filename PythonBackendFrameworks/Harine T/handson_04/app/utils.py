from flask import request, jsonify


def request_get_json():
    return request.get_json()


def make_response_json(data, status_code):
    return jsonify(data), status_code