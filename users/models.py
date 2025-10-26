from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="email")
    phone_number = models.CharField(
        max_length=15, null=True, blank=True, verbose_name="номер телефона"
    )
    avatar = models.ImageField(
        upload_to="avatars/", blank=True, null=True, verbose_name="фото"
    )
    country = models.CharField(max_length=50, blank=True, verbose_name="страна")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
