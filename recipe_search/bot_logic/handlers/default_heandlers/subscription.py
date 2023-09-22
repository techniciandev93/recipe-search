from telebot.types import Message
from recipe_search.bot_logic.loader import bot
from telebot import types


@bot.message_handler(commands=['Подписка'])
def bot_subscription(message: Message) -> None:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('/Подписаться')
    item2 = types.KeyboardButton('/Отписаться')
    item3 = types.KeyboardButton('/Меню')
    markup.add(item1, item2, item3,)

    bot.reply_to(message, 'Управление подпиской:\n'
                          'Вы можете подписаться и получать больше блюд, нажав Подписаться\n'
                          'Так же, если Вы хотите отписаться, в любой момент можете нажать Отписаться',
                 reply_markup=markup)
