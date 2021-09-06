from flask import Blueprint
from app.controllers.WelcomeController import WelcomeController


web_bp = Blueprint('web', __name__)

web_bp.route('/', methods=['GET'])(WelcomeController.index)
