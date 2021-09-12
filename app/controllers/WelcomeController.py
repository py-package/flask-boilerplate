from flask import render_template, request
from app.services.Storage import Storage


class WelcomeController():

    @staticmethod
    def index():
        data = {
            'title': 'Home Page',
        }
        return render_template("pages/index.html", **data)

    @staticmethod
    def about():
        data = {
            'title': 'About Page',
        }
        return render_template("pages/about.html", **data)

    @staticmethod
    def contact():
        data = {
            'title': 'Contact Page',
        }
        return render_template("pages/contact.html", **data)

    @staticmethod
    def file_upload():
        file = request.files['file']
        store = Storage.store(file)
        # Storage.delete("8c1f31de-105f-11ec-9291-8c8590d4499a")
        return {
            "key": store
        }
