from django.db import models


class TelegramUser(models.Model):
    name = models.CharField(max_length=250, blank=True, verbose_name='Имя пользователя')
    telegram_id = models.BigIntegerField(unique=True, verbose_name='ID пользователя в телеграмме')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    request_number = models.IntegerField(default=0, verbose_name='Количество запросов')
    subscription = models.BooleanField(default=False, verbose_name='Подписка')

    def __str__(self):
        return str(self.telegram_id)
