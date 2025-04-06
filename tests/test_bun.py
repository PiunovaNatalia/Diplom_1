from praktikum import Bun
import pytest
import allure
from .data import Data


class TestBun:
    @allure.title('Тестирование получения имени булочки')
    @allure.description(
        'Создается 2 объекта булочки, затем сраниваются имена '
        'из параметризованных данных с именами, которые были присвоены объектам'
    )
    @pytest.mark.parametrize('buns', Data.buns_data)
    def test_get_bun_name(self, buns):
        name, price = buns
        bun = Bun(name, price)

        assert bun.get_name() == name

    @allure.title('Тестирование получения цены булочки')
    @allure.description(
        'Создается 2 объекта булочки, затем сраниваются цены '
        'из параметризованных данных с ценами, которые были присвоены объектам'
    )
    @pytest.mark.parametrize('buns', Data.buns_data)
    def test_get_bun_price(self, buns):
        name, price = buns
        bun = Bun(name, price)

        assert bun.get_price() == price
