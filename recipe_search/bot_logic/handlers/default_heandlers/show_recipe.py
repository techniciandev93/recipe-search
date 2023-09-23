from telebot.types import Message
from recipe_search.bot_logic.loader import bot
from telebot import types
from recipe_search.models import Recipe
from telegram_users.services import get_request_number, add_requests_number, is_subscribe


@bot.callback_query_handler(func=lambda call : call.data == 'new_recipe')
def а(call):
    bot_show_dishes(call.message)


@bot.message_handler(func=lambda message: message.text == 'Показать блюда')
def bot_show_dishes(message: Message) -> None:
    request_numbers = get_request_number(message.chat.id)
    if request_numbers >= 3 and not is_subscribe(message.chat.id):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Меню подписки')
        markup.add(item1)
        bot.reply_to(message, f'У вас закончились пробные блюда,'
                              f' что-бы в дальнейшем пользоваться'
                              f' этим ботом необходимо оплатить подписку', reply_markup=markup)
    else:
        recipe = Recipe.objects.order_by('?').first()
        recipe_id = recipe.id
        recipe_name = recipe.recipe_name
        description = recipe.description
        markup = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton(text='Рецепт', callback_data=f"recipe_step_{recipe_id}")
        item2 = types.InlineKeyboardButton(text='Ингредиенты', callback_data=f"ingredients_for_{recipe_id}")
        item3 = types.InlineKeyboardButton(text='Следующее блюдо', callback_data="new_recipe")
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, f'{recipe_name}\n{description}', reply_markup=markup)
        add_requests_number(message.chat.id)
