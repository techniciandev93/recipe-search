from telebot import types
from telebot.types import Message
from recipe_search.bot_logic.loader import bot


@bot.message_handler(commands=['Меню'])
def bot_menu(message: Message) -> None:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('/Главная')
    item2 = types.KeyboardButton('/Пописка')

    markup.add(item1, item2)
    bot.reply_to(message.chat.id, 'Блюдо:', reply_markup=markup)
