from django.core.mail import send_mail
from django.conf import settings

from celery import shared_task


# Функция отправки приветственного собщения
@shared_task
def send_welcome_mail(user_email):
    subject = 'Приветственное письмо'
    message = 'Здравствуйте'
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user_email],
        fail_silently=False
    )
