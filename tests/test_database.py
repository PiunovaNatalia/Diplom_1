from praktikum import Database
from .data import Data


class TestDatabase:
    def test_database_available_buns(self):
        database = Database()
        available_buns = database.available_buns()

        assert len(available_buns) == Data.EXPECTED_AVAILABLE_BUNS

    def test_database_available_ingredients(self):
        database = Database()
        available_ingredients = database.available_ingredients()

        assert len(available_ingredients) == Data.EXPECTED_AVAILABLE_INGREDIENTS
