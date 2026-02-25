from django.test import TestCase
from .models import User

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@example.com", password="password")

    def test_user_email(self):
        self.assertEqual(self.user.email, "test@example.com")
