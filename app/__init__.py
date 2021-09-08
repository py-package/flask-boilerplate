from config import DevelopmentConfig
from flask import Flask, render_template
from flask_mail import Mail
from flask_orator import Orator
from celery import Celery

mail = Mail()
db = Orator()
celery = Celery(__name__, broker=DevelopmentConfig.CELERY_BROKER_URL, result_backend=DevelopmentConfig.RESULT_BACKEND)


def factory(config=DevelopmentConfig) -> Flask:
    app = Flask(__name__)

    app.template_folder = 'views'

    # load application configuration from config
    app.config.from_object(config)

    # initialize mail
    mail.init_app(app)
    mail.app = app

    # initialize database
    db.init_app(app)
    db.app = app

    # initialize celery
    celery.conf.update(app.config)

    register_blueprints(app)
    register_logging(app)

    return app


def register_blueprints(app):
    from routes.web import router as web_router
    from routes.api import router as api_router

    app.register_blueprint(web_router)
    app.register_blueprint(api_router)


def register_logging(app) -> None:
    import logging
    from flask.logging import default_handler
    from logging.handlers import RotatingFileHandler

    # Deactivate the default flask logger so that log messages don't get duplicated
    app.logger.removeHandler(default_handler)

    # Create a file handler object
    file_handler = RotatingFileHandler('flaskapp.log', maxBytes=16384, backupCount=20)

    # Set the logging level of the file handler object so that it logs INFO and up
    file_handler.setLevel(logging.INFO)

    # Create a file formatter object
    file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(filename)s: %(lineno)d]')

    # Apply the file formatter object to the file handler object
    file_handler.setFormatter(file_formatter)

    # Add file handler object to the logger
    app.logger.addHandler(file_handler)


def register_error_handlers(app) -> None:
    # 400 - Bad Request
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400

    # 403 - Forbidden
    @app.errorhandler(403)
    def forbidden(e):
        return render_template('errors/403.html'), 403

    # 404 - Page Not Found
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    # 405 - Method Not Allowed
    @app.errorhandler(405)
    def method_not_allowed(e):
        return render_template('errors/405.html'), 405

    # 500 - Internal Server Error
    @app.errorhandler(500)
    def server_error(e):
        return render_template('errors/500.html'), 500
