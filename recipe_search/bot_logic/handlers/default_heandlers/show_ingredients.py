from telebot.types import Message
from recipe_search.bot_logic.loader import bot
from telebot import types
from recipe_search.models import Recipe, Ingredient, RecipeStep


@bot.callback_query_handler(func=lambda call: call.data.startswith('ingredients_for'))
def handle_callback(call):
    recipe_id = call.data.split('_')[-1]
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Рецепт', callback_data=f"recipe_step_{recipe_id}")
    item2 = types.InlineKeyboardButton(text='Следующее блюдо', callback_data="new_recipe")
    markup.add(item1, item2)
    recipe = Recipe.objects.get(id=recipe_id)
    recipe_name = recipe.recipe_name
    ingredients = Ingredient.objects.filter(recipe_step__in=RecipeStep.objects.filter(recipe=recipe))
    ingredients_text = ''
    for n, ingredient in enumerate(ingredients):
        ingredients_text += f'{n+1}. {ingredient}: {ingredient.amount} {ingredient.unit}\n'
    bot.reply_to(call.message, f'{recipe_name}\n{ingredients_text}', reply_markup=markup)