from django.db import models


class BotAdmin(models.Model):
    telegram_user_id = models.BigIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.telegram_user_id)
