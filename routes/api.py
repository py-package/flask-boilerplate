from routes import create_router
from app.controllers.ApiController import ApiController


router = create_router('api', '/api')
router.route('/foo', methods=['GET'])(ApiController.index)
