from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_verification_email(email, token):
    subject = "Verify your email"
    message = f"Click the link to verify your email: http://127.0.0.1:8000/api/verify-email/?token={token}"
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
