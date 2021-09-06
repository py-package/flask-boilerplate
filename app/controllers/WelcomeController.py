from flask import render_template


class WelcomeController():

    @staticmethod
    def index():
        return render_template("index.html")
