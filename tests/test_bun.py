from praktikum import Bun
import pytest
from data import Data


class TestBun:
    @pytest.mark.parametrize('buns', Data.buns_data)
    def test_get_bun_name(self, buns):
        name, price = buns
        bun = Bun(name, price)

        assert bun.get_name() == name

    @pytest.mark.parametrize('buns', Data.buns_data)
    def test_get_bun_price(self, buns):
        name, price = buns
        bun = Bun(name, price)

        assert bun.get_price() == price
