from django.urls import path
from rest_framework.routers import DefaultRouter

from lms.apps import LmsConfig

from .views import (CourseViewSet, LessonCreateAPIView, LessonDestroyAPIView,
                    LessonListAPIView, LessonRetrieveAPIView,
                    LessonUpdateAPIView)

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r"course", CourseViewSet, basename="course")

urlpatterns = [
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson_create"),
    path("lessons/", LessonListAPIView.as_view(), name="lesson_list"),
    path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_get"),
    path(
        "lesson/update/<int:pk>/", LessonUpdateAPIView.as_view(), name="lesson_update"
    ),
    path(
        "lesson/delete/<int:pk>/", LessonDestroyAPIView.as_view(), name="lesson_delete"
    ),
]
urlpatterns += router.urls
