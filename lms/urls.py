from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LessonListCreateAPI, LessonRetrieveUpdateDeleteAPI
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register(r'courses', CourseViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lms.urls')),
    path('lessons/', LessonListCreateAPI.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonRetrieveUpdateDeleteAPI.as_view(), name='lesson-retrieve-update-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)