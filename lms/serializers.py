from rest_framework.serializers import ModelSerializer, SerializerMethodField

from lms.models import Course, Lessons


class LessonsSerializer(ModelSerializer):
    class Meta:
        model = Lessons
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    number_of_lessons = SerializerMethodField()
    lessons = LessonsSerializer(many=True, read_only=True)


@staticmethod
def get_number_of_lessons(instance):
    return instance.lessons.count()


class Meta:
    model = Course
    fields = "__all__"
