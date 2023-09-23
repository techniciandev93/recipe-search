from django.core.management import BaseCommand
from telebot.types import BotCommand
from recipe_search.bot_logic.loader import bot, default_commands
from recipe_search.bot_logic import handlers


class Command(BaseCommand):
    help = 'Команда для запуска Telegram-бота.'

    def handle(self, *args, **kwargs):
        bot.set_my_commands([BotCommand(*command) for command in default_commands])
        bot.polling(none_stop=True)
