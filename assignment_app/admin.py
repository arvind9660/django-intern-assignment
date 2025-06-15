from django.contrib import admin
from .models import TelegramUser

@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'chat_id')
    search_fields = ('username', 'first_name', 'chat_id')

