from praktikum import Database
import allure
from .data import Data


class TestDatabase:
    @allure.title('Тестирование метода available_buns')
    def test_database_available_buns(self):
        database = Database()
        available_buns = database.available_buns()

        assert len(available_buns) == Data.EXPECTED_AVAILABLE_BUNS

    @allure.title('Тестирование метода available_ingredients')
    def test_database_available_ingredients(self):
        database = Database()
        available_ingredients = database.available_ingredients()

        assert len(available_ingredients) == Data.EXPECTED_AVAILABLE_INGREDIENTS
