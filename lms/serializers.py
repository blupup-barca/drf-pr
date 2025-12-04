from rest_framework import serializers
from lms.models import Course, Lesson
from .validators import validate_links

class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для урока."""
    video_url = serializers.CharField(validators=[validate_links])

    class Meta:
        model = Lesson
        fields = [
            "name",
            "description",
            "video",
            "course",
        ]


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для курса."""

    lesson_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True, source="lesson_set")

    class Meta:
        model = Course
        fields = [
            "name",
            "description",
            "preview",
        ]

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()
