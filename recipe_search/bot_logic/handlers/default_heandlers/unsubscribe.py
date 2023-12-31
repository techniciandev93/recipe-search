from telebot.types import Message
from recipe_search.bot_logic.loader import bot
from telebot import types
from telegram_users.services import unsubscribe


@bot.message_handler(func=lambda message: message.text == 'Отписаться')
def bot_subscription(message: Message) -> None:

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Меню подписки')
    item2 = types.KeyboardButton('Показать блюда')
    markup.add(item1, item2, )

    if unsubscribe(message.from_user.id):
        bot.reply_to(message, 'Вы ещё не подписаны!', reply_markup=markup)
    else:
        bot.reply_to(message, 'Вы отписались от приложения', reply_markup=markup)
