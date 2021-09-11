from flask_mail import Message
from app import mail, celery
from flask import current_app


@celery.task(name='app.jobs.MailJob.send_mail_job')
def send_mail_job(message_data):
    """
    This function is used to send a test email to the user.
    """
    app = current_app._get_current_object()

    message = Message(subject=message_data['subject'],
                      recipients=[message_data['recipients']],
                      body=message_data['body'],
                      sender=app.config['MAIL_DEFAULT_SENDER'])

    mail.send(message)
