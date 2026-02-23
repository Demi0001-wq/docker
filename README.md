# LMS Project (Dockerized Django DRF)

This is a robust Learning Management System (LMS) built with Django Rest Framework, containerized with Docker, and protected by a professional CI/CD pipeline.

## Features
- Complete Course and Lesson management.
- Subscription system for course updates.
- Automated email notifications via Celery.
- Stripe payment integration.
- Automated testing and deployment via GitHub Actions.

## Local Setup

1. **Clone the repository**:
   ```bash
   git clone <repo_url>
   cd 35.2
   ```

2. **Configure environment**:
   Copy `.env.sample` to `.env` and fill in your credentials.
   ```bash
   cp .env.sample .env
   ```

3. **Run with Docker**:
   ```bash
   docker-compose up --build
   ```

4. **Run Tests**:
   ```bash
   python manage.py test
   ```

## Remote Deployment

The project is configured for automated deployment via GitHub Actions.

1. **GitHub Secrets**:
   Configure the following secrets in your GitHub repository:
   - `SERVER_HOST`: Your remote server IP.
   - `SERVER_USER`: Your SSH username.
   - `SERVER_SSH_KEY`: Your private SSH key.
   - `SERVER_SSH_PASSPHRASE`: (Optional) Your SSH key passphrase.

2. **CI/CD Pipeline**:
   Any push to the `main`, `develop`, or `homework-cicd-final` branches will trigger the pipeline:
   - **Lint & Test**: Runs Django tests and checks dependencies.
   - **Deploy**: If tests pass and you are pushing to `main` or `develop`, the code will be automatically deployed to your remote server.

## Technical Stack
- **Backend**: Django, Django Rest Framework
- **Database**: PostgreSQL (Production), SQLite3 (Local fallback)
- **Task Queue**: Celery, Redis
- **Containerization**: Docker, Docker Compose, Nginx
- **CI/CD**: GitHub Actions
