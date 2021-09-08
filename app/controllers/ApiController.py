from app.jobs.TestJob import send_test_job
from flask import jsonify


class ApiController():

    @staticmethod
    def index():
        response_data = {
            "foo": "bar",
        }

        message_data = {
            'subject': 'Hello from the flask app!',
            'body': 'This email was sent asynchronously using Celery.',
            'recipients': "",

        }
        send_test_job.apply_async(args=[message_data])

        return jsonify(response_data), 200
