from praktikum import Burger, Bun, Ingredient
import pytest
from .data import Data


class TestBurger:
    @pytest.mark.parametrize('buns', Data.buns_data)
    def test_burger_set_buns(self, buns):
        bun = Bun(*buns)
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun.name == bun.name

    @pytest.mark.parametrize('ingredients', Data.ingredients_data)
    def test_burger_add_ingredient(self, ingredients):
        ingredient = Ingredient(*ingredients)
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1

    @pytest.mark.parametrize('ingredients', Data.ingredients_data)
    def test_burger_remove_ingredient(self, ingredients):
        ingredient = Ingredient(*ingredients)
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1

        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_burger_move_ingredient(self):
        burger = Burger()

        for i in Data.ingredients_data:
            ingredient = Ingredient(*i)
            burger.add_ingredient(ingredient)

        initial_ingredients_list = burger.ingredients.copy()
        burger.move_ingredient(0, 1)
        after_moving_ingredients_list = burger.ingredients

        assert initial_ingredients_list[0] == after_moving_ingredients_list[1]

    @pytest.mark.parametrize('burger_data', Data.burger_data)
    def test_burger_get_price(self, burger_data):
        bun = burger_data['bun']
        ingredients = burger_data['ingredients']
        expected_price = burger_data['expected_price']

        burger = Burger()
        bun = Bun(*bun)
        burger.set_buns(bun)

        for ingredient in ingredients:
            ingredient = Ingredient(*ingredient)
            burger.add_ingredient(ingredient)

        assert burger.get_price() == expected_price

    @pytest.mark.parametrize('burger_data', Data.burger_data)
    def test_burger_get_price(self, burger_data):
        bun = burger_data['bun']
        ingredients = burger_data['ingredients']
        expected_receipt = burger_data['expected_receipt']

        burger = Burger()
        bun = Bun(*bun)
        burger.set_buns(bun)

        for ingredient in ingredients:
            ingredient = Ingredient(*ingredient)
            burger.add_ingredient(ingredient)

        assert burger.get_receipt() == expected_receipt