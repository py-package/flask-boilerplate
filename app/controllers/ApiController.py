from flask import jsonify


class ApiController():

    @staticmethod
    def index():
        response_data = {
            "foo": "bar",
        }

        return jsonify(response_data), 200
