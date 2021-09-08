from flask import render_template
from app import cache


class WelcomeController():

    @staticmethod
    @cache.memoize(timeout=60)
    def index():
        # cache.set('name', 'Yubaraj Shrestha')
        # print(cache.get('name'))
        return render_template("index.html")
