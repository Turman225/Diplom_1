import pytest
import data as data
from praktikum.bun import Bun
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun = Bun(data.bun_data[0], data.bun_data[1])
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(data.ingredients[1][0], data.ingredients[1][1], data.ingredients[1][2])
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(data.ingredients[2][0], data.ingredients[2][1], data.ingredients[2][2])
        burger.add_ingredient(ingredient)
        ingredient_index = burger.ingredients.index(ingredient)
        burger.remove_ingredient(ingredient_index)
        assert ingredient not in burger.ingredients

    def test_move_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(data.ingredients[3][0], data.ingredients[3][1], data.ingredients[3][2])
        ingredient_1 = Ingredient(data.ingredients[4][0], data.ingredients[4][1], data.ingredients[4][2])
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient_1)
        ingredient_index = burger.ingredients.index(ingredient)
        new_index = ingredient_index + 1
        burger.move_ingredient(ingredient_index, new_index)

        assert burger.ingredients.index(ingredient) == new_index

    def test_get_price(self):
        bun_price = 10
        ingredient_price = 10
        bun_mock = Mock()
        ingredient_mock = Mock()
        bun_mock.get_price.return_value = bun_price
        ingredient_mock.get_price.return_value = ingredient_price
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        assert burger.get_price() == bun_price * 2 + ingredient_price

    def test_get_receipt_bun(self):
        burger = Burger()
        bun = Bun(data.bun_data[0], data.bun_data[1])
        burger.set_buns(bun)
        assert burger.bun.get_name() in burger.get_receipt()

    @pytest.mark.parametrize("index", [0, 1])
    def test_get_receipt_ingredient(self, index):
        burger = Burger()
        bun = Bun(data.bun_data[0], data.bun_data[1])
        ingredient_1 = Ingredient(data.ingredients[3][0], data.ingredients[3][1], data.ingredients[3][2])
        ingredient_2 = Ingredient(data.ingredients[5][0], data.ingredients[5][1], data.ingredients[5][2])
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        assert burger.ingredients[index].get_name() in burger.get_receipt()

    def test_get_receipt_price(self):
        burger = Burger()
        bun = Bun(data.bun_data[0], data.bun_data[1])
        ingredient = Ingredient(data.ingredients[5][0], data.ingredients[5][1], data.ingredients[5][2])
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert str(burger.get_price()) in burger.get_receipt()