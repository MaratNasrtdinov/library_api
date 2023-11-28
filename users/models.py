from django.db import models
from django.contrib.auth.models import AbstractUser
from .tasks import send_welcome_mail


class UserModel(AbstractUser):
    username = models.CharField(max_length=64, unique=True, null=False)
    email = models.EmailField(max_length=64, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    first_name = None
    last_name = None


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        send_welcome_mail.delay(self.email)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
