from config import DevelopmentConfig
from flask import Flask
from flask_mail import Mail
from flask_orator import Orator

mail = Mail()
db = Orator()


def factory(config=DevelopmentConfig) -> Flask:
    app = Flask(__name__)

    app.template_folder = 'views'

    # load application configuration from config
    app.config.from_object(config)

    # initialize installed instances
    mail.init_app(app)
    mail.app = app

    db.init_app(app)
    db.app = app

    register_blueprints(app)

    return app


def register_blueprints(app):
    from routes.web import web_bp
    from routes.api import api_bp

    app.register_blueprint(web_bp)
    app.register_blueprint(api_bp)
