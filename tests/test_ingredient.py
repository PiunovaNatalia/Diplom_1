from praktikum import Ingredient
import pytest
from data import Data


class TestIngredient:
    @pytest.mark.parametrize('ingredients', Data.ingredients_data)
    def test_ingredient_get_name(self, ingredients):
        ingredient_type, name, price = ingredients
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredients', Data.ingredients_data)
    def test_ingredient_get_price(self, ingredients):
        ingredient_type, name, price = ingredients
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_price() == price

    @pytest.mark.parametrize('ingredients', Data.ingredients_data)
    def test_ingredient_get_type(self, ingredients):
        ingredient_type, name, price = ingredients
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type
