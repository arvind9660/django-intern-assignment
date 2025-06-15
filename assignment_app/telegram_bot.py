import os
import sys
import django
import logging
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv  

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assignment.settings')
django.setup()

from assignment_app.models import TelegramUser

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def start(update, context):
    user = update.message.from_user
    TelegramUser.objects.get_or_create(
        username=user.username,
        defaults={
            "chat_id": update.message.chat_id,
            "first_name": user.first_name
        }
    )
    update.message.reply_text(f"Hi {user.first_name or user.username}, you’ve been registered successfully!")

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
