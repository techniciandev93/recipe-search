from telebot.types import Message
from telebot import types
from recipe_search.bot_logic.loader import bot


@bot.message_handler(commands=['start'])
def bot_start(message: Message) -> None:
    """
    Команда /start. При вызове команды запускается бот и приветствуется пользователь.
    :param message: сообщение пользователя (ввод команды /start)
    :return: None
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('/start')
    item2 = types.KeyboardButton('/hello_world')

    markup.add(item1, item2,)

    bot.reply_to(message, f"Привет, {message.from_user.full_name}!\n"
                          f"\nЯ бот Домашний Шеф повар! Со мной ты можешь:\n"
                          f"\nПока только поздароваться с миром нажав /hello_world\n"
                          f"\nПриятного пользования!", reply_markup=markup)
