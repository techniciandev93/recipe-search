from recipe_search.models import Recipe, Ingredient


def get_recipe(recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return recipe


def get_ingredients(recipe_id):
    ingredients = Ingredient.objects.filter(recipe_step__recipe__id=recipe_id)
    return ingredients


def get_random_recipe():
    random_recipe = Recipe.objects.order_by('?').first()
    return random_recipe
