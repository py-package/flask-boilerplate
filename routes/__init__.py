from flask import Blueprint


def create_router(name, prefix):
    return Blueprint(name, __name__, url_prefix=prefix)
