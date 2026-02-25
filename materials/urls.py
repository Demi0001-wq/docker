from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register(r'courses', CourseViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
    path('course/subscribe/', SubscriptionAPIView.as_view(), name='course-subscribe'),
]
