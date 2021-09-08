from app.services import sign
from flask import render_template, request
from app import cache
from app.services.Storage import Storage
import json


class WelcomeController():

    @staticmethod
    @cache.memoize(timeout=60)
    def index():
        # cache.set('name', 'Yubaraj Shrestha')
        # print(cache.get('name'))

        return render_template("pages/index.html")

    @staticmethod
    def about():
        encrypted = sign().sign(json.dumps({
            "name": "Yubaraj Shrestha"
        }))
        print(encrypted)
        return render_template("pages/about.html")

    @staticmethod
    def contact():
        return render_template("pages/contact.html")

    @staticmethod
    def file_upload():
        file = request.files['file']
        store = Storage.store(file)
        # Storage.delete("8c1f31de-105f-11ec-9291-8c8590d4499a")
        return {
            "key": store
        }
