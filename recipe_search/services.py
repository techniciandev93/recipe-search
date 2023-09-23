from recipe_search.models import Recipe, Ingredient, RecipeStep


def get_recipe(recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return recipe


def get_ingredients(recipe):
    ingredients = Ingredient.objects.filter(recipe_step__in=RecipeStep.objects.filter(recipe=recipe))
    return ingredients


def get_random_recipe():
    random_recipe = Recipe.objects.order_by('?').first()
    return random_recipe
