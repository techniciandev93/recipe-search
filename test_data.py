import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'telegram_bot.settings')
import django

django.setup()
from recipe_search.models import RecipeCategory, Ingredient, Recipe, RecipeStep

recipe_data = [
    {
        'recipe_name': 'Тайский суп "Том Ям"',
        'description': 'Пикантный тайский суп с креветками и кокосовым молоком.',
        'author': 'Анна Иванова',
        'categories': ['Ужин', 'Закуски'],
        'steps': [
            {
                'step_description': 'Обжарьте лемонграсс и галангал (или имбирь) в кастрюле, добавьте листья лайма и чили-пасту.'
            },
            {
                'step_description': 'Залейте кокосовым молоком и куриной бульоном. Прокипятите суп.'
            },
            {
                'step_description': 'Добавьте креветки и грибы. Готовьте до готовности, пока креветки не станут розовыми.'
            },
            {
                'step_description': 'Подавайте, посыпанный свежей кинзой и нарезанным перцем чили.'
            },
            {
                'step_description': 'При желании, добавьте рисовые лепешки и листья каффир-лайма.'
            }
        ],
        'ingredients': [
            {
                'ingredient_name': 'Лемонграсс',
                'amount': 2,
                'unit': 'стебля'
            },
            {
                'ingredient_name': 'Галангал (или имбирь)',
                'amount': 2,
                'unit': 'ломтика'
            },
            {
                'ingredient_name': 'Листья лайма',
                'amount': 4,
                'unit': 'шт'
            },
            {
                'ingredient_name': 'Чили-паста',
                'amount': 2,
                'unit': 'чайные ложки'
            },
            {
                'ingredient_name': 'Кокосовое молоко',
                'amount': 400,
                'unit': 'мл'
            },
            {
                'ingredient_name': 'Куриной бульон',
                'amount': 500,
                'unit': 'мл'
            },
            {
                'ingredient_name': 'Креветки',
                'amount': 200,
                'unit': 'г'
            },
            {
                'ingredient_name': 'Грибы (шампиньоны)',
                'amount': 150,
                'unit': 'г'
            },
            {
                'ingredient_name': 'Кинза',
                'amount': 1,
                'unit': 'пучок'
            },
            {
                'ingredient_name': 'Перец чили',
                'amount': 1,
                'unit': 'шт'
            },
            {
                'ingredient_name': 'Рисовые лепешки (по желанию)',
                'amount': None,
                'unit': ''
            },
            {
                'ingredient_name': 'Листья каффир-лайма (по желанию)',
                'amount': None,
                'unit': ''
            }
        ]
    },
    {
        'recipe_name': 'Сырные гренки',
        'description': 'Хрустящие гренки с сыром и чесноком.',
        'author': 'Денис Морозов',
        'categories': ['Закуски', 'Полдник'],
        'steps': [
            {
                'step_description': 'Нарежьте хлеб на куски и обжарьте на сковороде до золотистой корки.'
            },
            {
                'step_description': 'Натрите обжаренные куски хлеба чесноком и посыпьте тертым сыром.'
            },
            {
                'step_description': 'Запекайте в духовке до золотистой корки.'
            },
            {
                'step_description': 'Подавайте горячими.'
            }
        ],
        'ingredients': [
            {
                'ingredient_name': 'Хлеб (белый или черный)',
                'amount': 4,
                'unit': 'ломтика'
            },
            {
                'ingredient_name': 'Чеснок',
                'amount': 2,
                'unit': 'зубчика'
            },
            {
                'ingredient_name': 'Твердый сыр (например, чеддер или гауда)',
                'amount': 100,
                'unit': 'г'
            },
            {
                'ingredient_name': 'Сливочное масло',
                'amount': 2,
                'unit': 'ст. ложки'
            }
        ]
    }
]

# Добавляем данные в базу данных
for recipe_info in recipe_data:
    recipe = Recipe.objects.create(
        recipe_name=recipe_info['recipe_name'],
        description=recipe_info['description'],
        author=recipe_info['author'],
    )

    # Добавляем категории к рецепту
    for category_name in recipe_info['categories']:
        category, created = RecipeCategory.objects.get_or_create(category_name=category_name)
        recipe.category.add(category)

    # Добавляем шаги рецепта
    for step_info in recipe_info['steps']:
        step = RecipeStep.objects.create(
            step_description=step_info['step_description'],
            recipe=recipe
        )

    # Добавляем ингредиенты к рецепту
    for ingredient_info in recipe_info['ingredients']:
        Ingredient.objects.create(
            ingredient_name=ingredient_info['ingredient_name'],
            amount=ingredient_info.get('amount', None),
            unit=ingredient_info.get('unit', ''),
            recipe_step=step
        )