from rest_framework import serializers
from .models import Course, Lesson



class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    number_of_lessons = serializers.IntegerField(source='num_lessons', read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'preview_image', 'description', 'number_of_lessons']

    def get_number_of_lessons(self, obj):
        return obj.lessons.count()