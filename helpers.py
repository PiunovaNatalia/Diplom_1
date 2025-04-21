from praktikum import Ingredient


def add_ingredients_to_burger(burger, ingredients):
    for ingredient in ingredients:
        i = Ingredient(*ingredient)
        burger.add_ingredient(i)

    return burger