# LMS Project

This is a backend project for a Learning Management System built with Django and Django REST Framework.

## Features
- User management with SimpleJWT authentication.
- Different user roles: Moderators and Owners.
- Materials management: Courses and Lessons.
- Subscription system for courses.
- Video link validation (YouTube only).
- Stripe payment integration.
- Professional API documentation with drf-spectacular (Swagger and Redoc).

## Tech Stack
- Django and Django REST Framework
- SimpleJWT
- Stripe API
- drf-spectacular
- SQLite (Local) / PostgreSQL (Remote)

## Local Setup
1. Install dependencies:
   pip install -r requirements.txt
2. Configure settings:
   Set STRIPE_API_KEY in config/settings.py or .env file.
3. Run migrations:
   python manage.py migrate
4. (Optional) Initial data:
   python manage.py fill_payments
5. Start server:
   python manage.py runserver

## Docker Setup
1. Create .env file from env.sample.
2. Build and start containers:
   docker-compose up --build -d

## CI/CD and Remote Deployment
This project uses GitHub Actions for automated testing and deployment.
- CI: Runs tests on push to main, develop, or homework-cicd-final.
- CD: Deploys to a remote server upon successful testing.

### GitHub Secrets
To use the CI/CD pipeline, configure these secrets in GitHub:
- SERVER_HOST: Server IP.
- SERVER_USER: SSH username.
- SERVER_SSH_KEY: Private SSH key.
- DJANGO_SECRET_KEY: Secret key for production.
- STRIPE_API_KEY: Your Stripe API key.

## API Endpoints
- /api/users/login/ - User Login
- /api/users/token/refresh/ - Refresh JWT
- /api/materials/courses/ - Course management
- /api/materials/lessons/ - Lesson management
- /api/materials/course/subscribe/ - Subscription toggle
- /api/users/payments/create/ - Create Checkout Session
- /api/users/payments/status/id/ - Check Payment Status

## Testing
Run tests locally:
python manage.py test

Run tests in Docker:
docker-compose exec backend python manage.py test
