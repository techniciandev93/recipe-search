from django.contrib import admin
from recipe_search.models import Ingredient, Recipe, RecipeCategory, RecipeStep


class RecipeStepAdmin(admin.TabularInline):
    model = RecipeStep
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeStepAdmin]


class IngredientAdmin(admin.TabularInline):
    model = Ingredient
    extra = 1


@admin.register(RecipeStep)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientAdmin]


admin.site.register(RecipeCategory)
admin.site.register(Ingredient)
