from django.conf import settings
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name="название")
    image = models.ImageField(
        upload_to="course_image/", blank=True, null=True, verbose_name="картинка"
    )
    description = models.TextField(verbose_name="описание")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="владелец",
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"
        ordering = ["title"]


class Lessons(models.Model):
    title = models.CharField(max_length=100, verbose_name="название")
    description = models.TextField(verbose_name="описание")
    image = models.ImageField(
        upload_to="lessons_image/", blank=True, null=True, verbose_name="картинка"
    )
    video_url = models.URLField(verbose_name="ссылка на видео", blank=True, null=True)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="lessons", verbose_name="курс"
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="владелец",
    )

    def __str__(self):
        return f"{self.title} ({self.course.title})"

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
        ordering = ["title", "course"]