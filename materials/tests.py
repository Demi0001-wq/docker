from django.test import TestCase
from .models import Course, Lesson

class MaterialTestCase(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name="Test Course", description="Test Description")
        self.lesson = Lesson.objects.create(name="Test Lesson", description="Test Lesson Description", course=self.course)

    def test_course_str(self):
        self.assertEqual(str(self.course), "Test Course")

    def test_lesson_str(self):
        self.assertEqual(str(self.lesson), "Test Lesson")
