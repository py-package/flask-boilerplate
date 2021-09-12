from app.controllers.AuthController import AuthController
from routes import create_router


router = create_router('auth', '/')
router.route('/login', methods=['GET', 'POST'])(AuthController.login)
router.route('/logout', methods=['GET'])(AuthController.logout)
router.route('/forgot-password', methods=['GET', 'POST'])(AuthController.forgot_password)
router.route('/home', methods=['GET'])(AuthController.home)
router.route('/profile', methods=['GET'])(AuthController.profile)
router.route('/settings', methods=['GET'])(AuthController.settings)
