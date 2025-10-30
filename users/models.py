from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Lessons, Course

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

class Payments(models.Model):
    METHOD_CHOICES = [
        ("Наличные", "Наличные"),
        ("Перевод", "Перевод"),
    ]

    user = models.ForeignKey(
        User,
        verbose_name="платежи",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    date = models.DateField(auto_now=True, verbose_name="дата платежа")
    course = models.ForeignKey(
        Course,
        related_name="paid_course",
        verbose_name="оплаченный курс",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    lessons = models.ForeignKey(
        Lessons,
        related_name="paid_lesson",
        verbose_name="оплаченный урок",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    payment_amount = models.IntegerField(verbose_name="сумма платежа")
    payment_method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    session_id_course = models.CharField(
        max_length=250, null=True, blank=True, verbose_name="id сессии"
    )
    link_course = models.URLField(
        max_length=400, null=True, blank=True, verbose_name="ссылка на оплату"
    )
    session_id_lesson = models.CharField(
        max_length=250, null=True, blank=True, verbose_name="id сессии"
    )
    link_lesson = models.URLField(
        max_length=400, null=True, blank=True, verbose_name="ссылка на оплату"
    )

    def __str__(self):
        return f"{self.user.email} — {self.payment_amount} ₽ — {self.date}"