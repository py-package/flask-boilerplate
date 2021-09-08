from routes import create_router
from app.controllers.WelcomeController import WelcomeController


router = create_router('web', '/')
router.route('/', methods=['GET'])(WelcomeController.index)
