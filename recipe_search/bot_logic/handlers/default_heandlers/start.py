from telebot.types import Message
from telebot import types
from recipe_search.bot_logic.loader import bot
from telegram_users.services import create_user


@bot.message_handler(commands=['start', 'Главная'])
def bot_start(message: Message) -> None:
    """
    Команда /start. При вызове команды запускается бот и приветствуется пользователь.
    :param message: сообщение пользователя (ввод команды /start)
    :return: None
    """
    create_user(message.from_user.id, message.from_user.full_name)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Меню подписки')
    item2 = types.KeyboardButton('Показать блюда')

    markup.add(item1, item2, )

    bot.reply_to(message, f"Привет, {message.from_user.full_name}!\n"
                          f"Это бот для кулинаров без воображения. "
                          f"Он поможет тебе выбрать блюда на любой случай. "
                          f"Сервис платный, но ты можешь протестить, посмотрев 3 пробных блюда.\n"
                          f"Приятного пользования!", reply_markup=markup)
