from app import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash


class User(db.Model, UserMixin):

    __fillable__ = ['name', 'email', 'password', 'email_verified_at']

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
