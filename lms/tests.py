from rest_framework.test import APITestCase
from rest_framework import status

from lms.models import Course, Lesson
from users.models import CustomUser


class TestCourseLesson(APITestCase):
    """ Тест курса и урока. """

    def setUp(self) -> None:
        """ Создание тестового пользователя для авторизации. """

        self.user = CustomUser.objects.create_user(
            email='test@test.com',
            username='TesTUser',
            password='password123'
        )

        self.course = Course.objects.create(
            name='Test_Course_1',
            description='Test_Course_1',
            owner=self.user
        )

        self.lesson = Lesson.objects.create(
            name='Test_Lesson_3',
            description='Test_Lesson_3',
            owner=self.user,
            course=self.course,
        )

        self.client.force_authenticate(user=self.user)

    def test_create_course(self):
        """Тест создание курса."""

        data = {
            "name": "Test_course_2",
            "description": "Test_course_2",
            "owner": self.user.id,
        }

        response = self.client.post("/course/", data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        expected_response = {
            "name": "Test_course_2",
            "description": "Test_course_2",
            "preview": None,
            "count_of_lessons": 0,
            "info_lessons": [],
            "is_subscribed": False
        }

        self.assertEqual(response.json(), expected_response)

        self.assertTrue(Course.objects.all().exists())

    def test_create_lesson(self):
        data = {
            "name": "Test_lesson",
            "description": "Test_lesson",
            "course": self.course.pk,
            "video_url": "http://youtube.com/",
        }
        response = self.client.post("/lesson/create/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        if 'id' in response.data:
            lesson_id = response.data['id']
            created_lesson = Lesson.objects.get(pk=lesson_id)
            self.assertEqual(created_lesson.name, 'Test_lesson')
            self.assertEqual(created_lesson.description, 'Test_lesson')
            self.assertEqual(created_lesson.owner, self.user)
            self.assertEqual(created_lesson.course, self.course)

    def test_update_lesson(self):
        """ Тест обновление урока. """

        self.user.is_staff = True
        self.user.save()

        updated_data = {
            'name': 'Updated_test_lesson',
            'description': 'Updated_test_description',
            'course': self.course.id,
        }

        response = self.client.patch(f'/lesson/update/{self.lesson.id}/', data=updated_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_lesson = Lesson.objects.get(id=self.lesson.id)

        self.assertEqual(updated_lesson.name, 'Updated_test_lesson')
        self.assertEqual(updated_lesson.description, 'Updated_test_description')
        self.assertEqual(updated_lesson.course, self.course)

    def test_delete_lesson(self):
        response = self.client.delete(f'/lesson/delete/{self.lesson.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Lesson.DoesNotExist):
            Lesson.objects.get(id=self.lesson.id)