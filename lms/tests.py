from lms.models import Course, Lesson
from users.models import CustomUser
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class LessonsTestCase(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(email="admin@sky.pro")
        self.course = Course.objects.create(
            title="Прыжки",
            description="В курсе представлены маленькие и большие прыжки",
        )
        self.lesson = Lesson.objects.create(
            title="Saute",
            description="Маленькие прыжки",
            owner=self.user,
            course=self.course,
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("lms:lessons_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.lesson.title)

    def test_lesson_create(self):
        url = reverse("lms:lessons_create")
        data = {
            "title": "Общая физическая подготовка",
            "description": "Урок содержит упражнения для развития физической формы ученика",
            "course": self.course.pk,
            "video_url": "http://youtube.com/",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse("lms:lessons_update", args=(self.lesson.pk,))
        data = {
            "title": "Прыжки. От простого к сложному",
            "description": "В курсе представлены маленькие и большие прыжки",
            "course": self.course.pk,
            "link_to_video": "http://youtube.com/",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Прыжки. От простого к сложному")

    def test_lesson_delete(self):
        url = reverse("lms:lessons_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("lms:lessons_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "title": self.lesson.title,
                    "course": self.course.pk,
                    "owner": self.user.pk,
                    "video_url": self.lesson.video_url,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
