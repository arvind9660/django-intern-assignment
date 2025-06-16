

**Django Internship Assignment – Backend Development Project**

This project demonstrates backend development using Django, Django REST Framework, JWT authentication, Celery with Redis, and Telegram Bot integration. Submitted as part of an internship task.

Features Implemented

- Django REST API using Django REST Framework (DRF)
- JWT-based Authentication with SimpleJWT
- Telegram Bot integration to collect user data
- Celery with Redis for background tasks
- Environment variable management with dotenv
- Admin panel for managing data

Tech Stack

- Language: Python 3.x
- Framework: Django, Django REST Framework
- Authentication: JWT (SimpleJWT)
- Background Tasks: Celery + Redis
- Bot API: Telegram Bot API
- Database: SQLite or MySQL (your choice)
- Config: dotenv / decouple

Project Structure
|
assignment/  
├── assignment/ (Django settings)  
├── assignment_app/ (API and Telegram Bot)  
├── manage.py  
├── requirements.txt  
└── .env

Setup Instructions

1. Clone the repository and create virtual environment

git clone <https://github.com/arvind9660/django-intern-assignment>  
cd your-repo  
python -m venv venv  
venv\\Scripts\\activate

1. Install the dependencies

pip install -r requirements.txt

1. Create a .env file and add the following keys

SECRET_KEY=your-secret-key  
DEBUG=True  
TELEGRAM_BOT_TOKEN=your-telegram-bot-token

Run the Project

1. Apply database migrations

python manage.py migrate

1. Start the development server

python manage.py runserver

Admin Access

To access the admin panel, create a superuser:

python manage.py createsuperuser

Then go to: <http://127.0.0.1:8000/admin>

Telegram Bot Instructions

1. Create a bot using BotFather on Telegram
2. Copy the bot token into your .env file
3. Run the bot using:

python assignment_app/telegram_bot.py

When a user sends /start command, the bot saves:

- username
- first_name
- chat_id

into the TelegramUser model.

TelegramUser Model

from django.db import models

class TelegramUser(models.Model):  
username = models.CharField(max_length=150, unique=True, null=True, blank=True)  
first_name = models.CharField(max_length=150, blank=True, null=True)  
chat_id = models.CharField(max_length=50, unique=True)

python

CopyEdit

def \__str_\_(self):

return self.username or self.first_name or f"User {self.id}"

JWT Authentication Endpoints

1. To get token:  
    POST /api/token/  
    Body: username and password
2. To refresh token:  
    POST /api/token/refresh/

Add token in header while using APIs:

Authorization: Bearer your_token

Celery and Redis

1. Start Redis server on your system
2. Start Celery worker:

celery -A assignment worker --loglevel=info

This will allow background jobs to run asynchronously.

Summary

- Fully working Telegram bot and API
- Clean database integration
- Secure authentication with JWT
- Background processing using Celery
- Deployment-ready project structure

Author

Name: Arvind Singh  
Project: Django Internship Backend Assignment  
Email: arvindsinghbhati9660@gmail.com  
