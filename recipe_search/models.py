from django.db import models


class RecipeCategory(models.Model):
    category_name = models.CharField(max_length=50, unique=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.category_name


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=255, unique=True, verbose_name='Рецепт')
    description = models.TextField(verbose_name='Описание')
    category = models.ManyToManyField(RecipeCategory, verbose_name='Категория')
    recipe_image = models.ImageField(upload_to='images', null=True, blank=True, verbose_name='Изображение')
    author = models.CharField(max_length=255, verbose_name='Автор')

    def __str__(self):
        return self.recipe_name


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=255, verbose_name='Ингридиент')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Количество ингредиентов')
    unit = models.CharField(max_length=10, verbose_name='Единица измерения')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='Рецепт')

    def __str__(self):
        return self.ingredient_name
