from django.core.management.base import BaseCommand
from users.models import Payment, User
from materials.models import Course, Lesson
from datetime import date

class Command(BaseCommand):
    help = 'Fill the database with sample payment data'

    def handle(self, *args, **options):
        # Ensure we have a user
        user, _ = User.objects.get_or_create(email='admin@example.com')
        if _:
            user.set_password('admin123')
            user.is_staff = True
            user.is_superuser = True
            user.save()

        # Ensure we have a course and lesson
        course, _ = Course.objects.get_or_create(name='Django Basics', description='Learn the basics of Django.')
        lesson, _ = Lesson.objects.get_or_create(name='Models', description='Working with models', course=course)

        # Create sample payments
        Payment.objects.get_or_create(
            user=user,
            payment_date=date.today(),
            paid_course=course,
            payment_amount=5000.00,
            payment_method='transfer'
        )

        Payment.objects.get_or_create(
            user=user,
            payment_date=date.today(),
            paid_lesson=lesson,
            payment_amount=1000.00,
            payment_method='cash'
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated payment data'))
