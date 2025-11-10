from django.core.management.base import BaseCommand
from users.models import Payment, CustomUser
from lms.models import Course, Lesson
import random


class Command(BaseCommand):
    help = 'Создание записей платежей для тестирования.'

    def handle(self, *args, **options):
        try:
            user = CustomUser.objects.first()
            courses = list(Course.objects.all())
            lessons = list(Lesson.objects.all())

            for _ in range(5):  # Генерируем 5 случайных платежей
                if random.choice([True, False]):
                    paid_item = random.choice(courses)
                    lesson_id = None
                else:
                    paid_item = random.choice(lessons)
                    lesson_id = paid_item.id

                Payment.objects.create(
                    user=user,
                    paid_course=paid_item if isinstance(paid_item, Course) else None,
                    paid_lesson=paid_item if isinstance(paid_item, Lesson) else None,
                    amount=random.randint(100, 1000),
                    method=random.choice(['cash', 'transfer'])
                )
            print("Данные успешно загружены.")
        except Exception as e:
            print(f"Ошибка загрузки данных: {e}")