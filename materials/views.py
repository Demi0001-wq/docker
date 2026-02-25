from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Course, Lesson, Subscription
from .serializers import *
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    def perform_create(self, serializer): serializer.save(owner=self.request.user)
class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
class SubscriptionAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, *args, **kwargs):
        user, course_id = self.request.user, self.request.data.get('course')
        from django.shortcuts import get_object_or_404
        course_item = get_object_or_404(Course, pk=course_id)
        subs_item = Subscription.objects.filter(user=user, course=course_item)
        if subs_item.exists():
            subs_item.delete()
            message = 'subscription deleted'
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = 'subscription added'
        return Response({"message": message})
