from django.contrib import admin
from recipe_search.models import Ingredient, Recipe, RecipeCategory


class IngredientAdmin(admin.TabularInline):
    model = Ingredient
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientAdmin]


admin.site.register(RecipeCategory)
admin.site.register(Ingredient)
