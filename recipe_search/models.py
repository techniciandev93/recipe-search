from django.db import models


class RecipeCategory(models.Model):
    category_name = models.CharField(max_length=50, unique=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.category_name


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=255, unique=True, verbose_name='Рецепт')
    description = models.TextField(verbose_name='Описание')
    category = models.ManyToManyField(RecipeCategory, verbose_name='Категория', related_name='recipes')
    recipe_image = models.ImageField(upload_to='images', null=True, blank=True, verbose_name='Изображение')
    author = models.CharField(max_length=255, verbose_name='Автор')

    def __str__(self):
        return self.recipe_name


class RecipeStep(models.Model):
    step_description = models.TextField(verbose_name='Описание шага')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='Рецепт', related_name='recipe_steps')

    def __str__(self):
        return self.step_description


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=255, verbose_name='Ингрeдиент')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Количество ингредиентов', null=True,
                                 blank=True)
    unit = models.CharField(max_length=10, verbose_name='Единица измерения', blank=True)
    recipe_step = models.ForeignKey(RecipeStep, on_delete=models.CASCADE, verbose_name='Шаг рецепта',
                                    related_name='ingredients')

    def __str__(self):
        return self.ingredient_name
