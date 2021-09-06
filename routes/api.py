from flask import Blueprint
from app.controllers.ApiController import ApiController


api_bp = Blueprint('api', __name__, url_prefix='/api')

api_bp.route('/foo', methods=['GET'])(ApiController.index)
