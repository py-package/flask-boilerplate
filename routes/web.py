from routes import create_router
from app.controllers.WelcomeController import WelcomeController


router = create_router('web', '/')
router.route('/', methods=['GET'])(WelcomeController.index)
router.route('/about', methods=['GET'])(WelcomeController.about)
router.route('/contact', methods=['GET'])(WelcomeController.contact)
router.route('/storage', methods=['POST'])(WelcomeController.file_upload)
