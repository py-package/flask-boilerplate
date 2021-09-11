from app.models.User import User
from app.forms import ForgotPasswordForm, LoginForm
from flask import render_template, redirect, request
from flask_login import login_user, logout_user, login_required, current_user


class AuthController():

    @staticmethod
    def login():
        form = LoginForm()
        if request.method == 'GET':
            return render_template('pages/auth/login.html', title='Login', form=form)
        else:
            if form.validate_on_submit():
                email = form.data['email']
                password = form.data['password']

                user = User.where("email", email).first()
                if user is None:
                    return render_template('pages/auth/login.html', title='Login', form=form, message="User not found!")

                if user.check_password(password):
                    login_user(user)
                    return redirect('/home')

            return render_template('pages/auth/login.html', title='Login', form=form, message="User not found!")

    def register():
        """
        Register a user
        """
        return redirect('/')

    def forgot_password():
        """
        Forgot password
        """
        form = ForgotPasswordForm()
        if request.method == 'GET':
            return render_template('pages/auth/forgot_password.html', title='Forgot Password', form=form)
        else:
            if form.validate_on_submit():
                email = form.data['email']
                user = User.where("email", email).first()
                if user is None:
                    return render_template('pages/auth/forgot_password.html', title="Forgot Password", form=form, message="User not found!")
                user.send_password_reset_email()
                return render_template('pages/auth/forgot_password.html', title="Forgot Password", form=form, message="User not found!")
            return render_template('pages/auth/forgot_password.html', title="Forgot Password", form=form, message="Invalid parameters!")

    @login_required
    def logout():
        logout_user()
        return redirect('/')

    @login_required
    def profile():
        return render_template('pages/auth/profile.html', title='Profile', user=current_user)

    @login_required
    def home():
        return render_template('pages/auth/home.html', title='Home', user=current_user)
