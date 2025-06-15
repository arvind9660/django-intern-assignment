from django.db import models
class TelegramUser(models.Model):
    username = models.CharField(max_length=150, unique=True,null=True,blank=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    chat_id = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.username or self.first_name or f"User {self.id}"