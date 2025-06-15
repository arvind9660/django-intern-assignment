# assignment_app/task.py

from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(user_email):
    send_mail(
        'Welcome!',
        'Thanks for registering on our site.',
        'your_email@gmail.com',      
        [user_email],              
        fail_silently=True,
    )
