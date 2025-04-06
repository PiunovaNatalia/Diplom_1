from praktikum import Ingredient
import pytest
import allure
from .data import Data


class TestIngredient:
    @allure.title('Тестирование получения имени ингредиента')
    @allure.description(
        'Создается 2 объекта ингредиента, затем сраниваются имена '
        'из параметризованных данных с именами, которые были присвоены объектам'
    )
    @pytest.mark.parametrize('ingredients', Data.ingredients_data)
    def test_ingredient_get_name(self, ingredients):
        ingredient_type, name, price = ingredients
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_name() == name

    @allure.title('Тестирование получения цены ингредиента')
    @allure.description(
        'Создается 2 объекта ингредиента, затем сраниваются цены '
        'из параметризованных данных с ценами, которые были присвоены объектам'
    )
    @pytest.mark.parametrize('ingredients', Data.ingredients_data)
    def test_ingredient_get_price(self, ingredients):
        ingredient_type, name, price = ingredients
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_price() == price

    @allure.title('Тестирование получения типа ингредиента')
    @allure.description(
        'Создается 2 объекта ингредиента, затем сраниваются типы '
        'из параметризованных данных с типами, которые были присвоены объектам'
    )
    @pytest.mark.parametrize('ingredients', Data.ingredients_data)
    def test_ingredient_get_type(self, ingredients):
        ingredient_type, name, price = ingredients
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type


