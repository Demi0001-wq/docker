from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model

@shared_task
def deactivate_inactive_users():
    """Blocks users who haven't logged in for more than a month (30 days)."""
    User = get_user_model()
    one_month_ago = timezone.now() - timedelta(days=30)
    
    # We find users who logged in more than 30 days ago AND are still active.
    # Users who have never logged in (last_login is None) are also checked 
    # if they were created more than 30 days ago.
    inactive_users = User.objects.filter(
        last_login__lt=one_month_ago,
        is_active=True
    )
    
    count = inactive_users.count()
    if count > 0:
        inactive_users.update(is_active=False)
        print(f"Successfully deactivated {count} inactive users.")
    else:
        print("No inactive users found to deactivate.")
