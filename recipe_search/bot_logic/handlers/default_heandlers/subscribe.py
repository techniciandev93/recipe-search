from telebot.types import Message
from recipe_search.bot_logic.loader import bot
from telebot import types
from telegram_users.services import subscribe


@bot.message_handler(func=lambda message: message.text == 'Подписаться')
def bot_subscription(message: Message) -> None:

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Меню подписки')
    item2 = types.KeyboardButton('Показать блюда')
    markup.add(item1, item2, )

    if subscribe(message.chat.id):
        bot.reply_to(message, 'Вы уже подписаны!', reply_markup=markup)
    else:
        bot.reply_to(message, 'Вы успешно подписались!', reply_markup=markup)

