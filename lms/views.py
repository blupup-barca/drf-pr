from rest_framework import viewsets
from .models import Course, Lessons
from .serializers import CourseSerializer, LessonsSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LessonCreateAPIView(CreateAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()

class LessonListAPIView(ListAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()

class LessonUpdateAPIView(UpdateAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()

class LessonDestroyAPIView(DestroyAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()

class LessonRetrieveAPIView(RetrieveAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()