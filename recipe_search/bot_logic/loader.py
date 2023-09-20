from django.conf import settings
from telebot import StateMemoryStorage, TeleBot

BOT_TOKEN = settings.TELEGRAM_BOT_API_TOKEN

state_storage = StateMemoryStorage()
bot = TeleBot(BOT_TOKEN, state_storage=state_storage)
