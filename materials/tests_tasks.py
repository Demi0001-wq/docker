from django.test import TestCase
from unittest.mock import patch
from materials.tasks import send_course_update_email
from materials.models import Course, Subscription
from users.models import User
from django.core import mail

class CeleryTasksTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', password='password')
        self.course = Course.objects.create(name='Test Course', description='Test Description', owner=self.user)
        Subscription.objects.create(user=self.user, course=self.course)

    @patch('materials.tasks.Course.objects.get')
    @patch('materials.tasks.Subscription.objects.filter')
    def test_send_course_update_email(self, mock_sub_filter, mock_course_get):
        # Mock Course
        mock_course_get.return_value = self.course
        
        # Mock Subscription list
        mock_sub = Subscription(user=self.user, course=self.course)
        mock_sub_filter.return_value = [mock_sub]
        
        # Run the task directly (not as background task for test)
        send_course_update_email(self.course.id)
        
        # Check if email was sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, f"Update: Course '{self.course.name}' has been updated")
        self.assertIn(self.user.email, mail.outbox[0].to)

class UserTasksTestCase(TestCase):
    def setUp(self):
        from django.utils import timezone
        from datetime import timedelta
        
        # Active user
        self.active_user = User.objects.create_user(email='active@example.com', password='password')
        
        # Inactive user (logged in 31 days ago)
        self.inactive_user = User.objects.create_user(email='inactive@example.com', password='password')
        self.inactive_user.last_login = timezone.now() - timedelta(days=31)
        self.inactive_user.save()

    def test_deactivate_inactive_users(self):
        from users.tasks import deactivate_inactive_users
        
        deactivate_inactive_users()
        
        self.inactive_user.refresh_from_db()
        self.active_user.refresh_from_db()
        
        self.assertFalse(self.inactive_user.is_active)
        self.assertTrue(self.active_user.is_active)
