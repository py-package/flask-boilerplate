from flask import Blueprint, request, jsonify, render_template
from werkzeug.utils import redirect
from flask_login import login_user


def create_router(name, prefix) -> Blueprint:
    blueprint = Blueprint(name, __name__, url_prefix=prefix)
    return blueprint
