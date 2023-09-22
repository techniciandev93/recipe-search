from telebot.types import Message
from recipe_search.bot_logic.loader import bot
from telebot import types


@bot.message_handler(commands=['Отписаться'])
def bot_subscription(message: Message) -> None:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('/Меню')
    item2 = types.KeyboardButton('/Главная')
    markup.add(item1, item2)
    bot.reply_to(message, 'Вы отписались от приложения', reply_markup=markup)