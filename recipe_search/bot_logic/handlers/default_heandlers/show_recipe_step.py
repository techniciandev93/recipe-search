from telebot.types import Message
from recipe_search.bot_logic.loader import bot
from telebot import types
from recipe_search.services import get_recipe


@bot.callback_query_handler(func=lambda call: call.data.startswith('recipe_step'))
def handle_callback(call):
    recipe_id = call.data.split('_')[-1]
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Ингредиенты', callback_data=f"ingredients_for_{recipe_id}")
    item2 = types.InlineKeyboardButton(text='Следующее блюдо', callback_data="new_recipe")
    markup.add(item1, item2)
    recipe = get_recipe(recipe_id)
    recipe_name = recipe.recipe_name
    recipe_steps = recipe.recipe_steps.all()
    recipe_steps_text = ''
    for n, recipe_step in enumerate(recipe_steps):
        recipe_steps_text += f'Шаг {n + 1}:\n {recipe_step}\n'

    bot.reply_to(call.message, f'{recipe_name}\n{recipe_steps_text}', reply_markup=markup)
