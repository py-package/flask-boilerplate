from app import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash
from .defaults import Defaults


class User(db.Model, Defaults, UserMixin):

    __tablename__ = 'users'

    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    email_verified_at = db.Column(db.DateTime, unique=False, nullable=True)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def send_password_reset_email(self):
        from app.jobs.MailJob import send_mail_job
        message_data = {
            'subject': 'Reset Password',
            'body': 'This email was sent asynchronously using Celery.',
            'recipients': self.email,
        }
        send_mail_job.apply_async(args=[message_data])

    def __repr__(self) -> str:
        return '<User %r>' % self.name
