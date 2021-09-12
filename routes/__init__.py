from flask import Blueprint


def create_router(name, prefix) -> Blueprint:
    blueprint = Blueprint(name, __name__, url_prefix=prefix)
    return blueprint
