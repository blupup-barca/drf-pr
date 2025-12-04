from django.shortcuts import get_object_or_404
from rest_framework.filters import OrderingFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from lms.models import Course, Lesson, Subscribe
from lms.serializers import CourseSerializer, LessonSerializer
from lms.paginators import CustomPagination
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsModer, IsOwner


# region CRUD для курса


class CourseCreateAPIView(CreateAPIView):
    """Создание курса."""

    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Заполнение поля owner данными текущего пользователя."""

        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()


class CourseViewSet(ModelViewSet):
    """Представление для курса."""

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]

    pagination_class = CustomPagination

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (~IsModer,)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = (IsModer | IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (~IsModer | IsOwner,)
        return super().get_permissions()


class CourseUpdateAPIView(UpdateAPIView):
    """Обновление курса."""

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsModer]


class CourseDeleteAPIView(DestroyAPIView):
    """Удаление курса."""

    serializer_class = CourseSerializer
    permission_classes = [IsOwner]


# endregion


# region CRUD для урока
class LessonCreateAPIView(CreateAPIView):
    """Создание урока."""

    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Заполнение поля owner данными текущего пользователя."""

        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(ListAPIView):
    """Просмотр списка уроков."""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    search_fields = ["name", "description", "course"]
    ordering_fields = ["name"]
    ordering = ["-name"]
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination


class LessonRetrieveAPIView(RetrieveAPIView):
    """Просмотр одного урока."""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonUpdateAPIView(UpdateAPIView):
    """Обновление одного урока."""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModer]


class LessonDeleteAPIView(DestroyAPIView):
    """Удаление урока."""

    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]


class SubscribeView(APIView):
    """Добавление и удаление подписки пользователя."""

    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        course_id = request.data.get("course_id")
        course = get_object_or_404(Course, id=course_id)

        subscribe = Subscribe.objects.filter(user=user, course=course)

        if subscribe.exists():
            subscribe.delete()
            return Response(status=204)
        else:
            Subscribe.objects.create(user=user, course=course)
            return Response(status=201)
