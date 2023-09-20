from django.db import models


class TelegramUser(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    telegram_id = models.BigIntegerField(unique=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.telegram_id
