from telebot import types
from telebot.types import Message
from recipe_search.bot_logic.loader import bot


@bot.message_handler(func=lambda message: message.text == 'Меню')
def bot_menu(message: Message) -> None:

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Меню подписки')
    item2 = types.KeyboardButton('Показать блюда')
    markup.add(item1, item2, )

    bot.send_message(message.chat.id, 'Главное меню', reply_markup=markup)
