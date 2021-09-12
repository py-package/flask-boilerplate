from config import DevelopmentConfig, TestingConfig
from flask import Flask, render_template
from flask_mail import Mail
from flask_orator import Orator
from celery import Celery
from flask_caching import Cache
from depot.manager import DepotManager
from flask_login import LoginManager

mail = Mail()
db = Orator()
celery = Celery(__name__, broker=DevelopmentConfig.CELERY_BROKER_URL, result_backend=DevelopmentConfig.RESULT_BACKEND)
cache = Cache()
login_manager = LoginManager()

DepotManager.configure(name='default', config={
    'depot.storage_path': 'storage/public'
}, prefix='depot.')


def factory(config=DevelopmentConfig) -> Flask:
    app = Flask(__name__)

    app.template_folder = 'views'

    # load application configuration from config
    app.config.from_object(config)

    # initialize cache
    cache_config = {
        'CACHE_TYPE': 'RedisCache',
        'CACHE_REDIS_HOST': config.REDIS_HOST,
    }
    # Enable to use Redis as cache backend
    # cache.init_app(app, config=cache_config)

    # initialize mail
    mail.init_app(app)
    mail.app = app

    # initialize database
    db.init_app(app)
    db.app = app

    # initialize login_manager
    register_login_manager(app)

    if config is not TestingConfig:
        # configure depotmanager
        app.wsgi_app = DepotManager.make_middleware(app.wsgi_app, mountpoint="/public")

    # initialize celery
    celery.conf.update(app.config)

    register_blueprints(app)
    register_logging(app)
    register_error_handlers(app)

    return app


def register_login_manager(app):
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    login_manager.session_protection = 'strong'
    login_manager.login_message = 'Please login to access this page.'
    login_manager.login_message_category = 'info'
    login_manager.needs_refresh_message = 'To protect your account, please reauthenticate to access this page.'
    login_manager.needs_refresh_message_category = 'info'
    login_manager.refresh_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        from app.models.User import User
        return User.find(user_id)


def register_blueprints(app):
    from routes.auth import router as auth_router
    from routes.web import router as web_router
    from routes.api import router as api_router

    app.register_blueprint(auth_router)
    app.register_blueprint(web_router)
    app.register_blueprint(api_router)


def register_logging(app) -> None:
    import logging
    from flask.logging import default_handler
    from logging.handlers import RotatingFileHandler

    # Deactivate the default flask logger so that log messages don't get duplicated
    app.logger.removeHandler(default_handler)

    # Create a file handler object
    file_handler = RotatingFileHandler('storage/logs/flaskapp.log', maxBytes=16384, backupCount=20)

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
        data = {
            "title": 400,
            "message": "Bad Request"
        }
        return render_template('errors/400.html', **data), 400

    # 403 - Forbidden
    @app.errorhandler(403)
    def forbidden(e):
        data = {
            "title": 403,
            "message": "Forbidden"
        }
        return render_template('errors/403.html', **data), 403

    # 404 - Page Not Found
    @app.errorhandler(404)
    def page_not_found(e):
        data = {
            "title": 404,
            "message": "Page not found"
        }
        return render_template('errors/404.html', **data), 404

    # 405 - Method Not Allowed
    @app.errorhandler(405)
    def method_not_allowed(e):
        data = {
            "title": 405,
            "message": "Method Not Allowed"
        }
        return render_template('errors/405.html', **data), 405

    # 500 - Internal Server Error
    @app.errorhandler(500)
    def server_error(e):
        data = {
            "title": 500,
            "message": "Internal Server Error"
        }
        return render_template('errors/500.html', **data), 500
