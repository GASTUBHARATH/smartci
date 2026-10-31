import pytest

from src.inventory import Inventory


def test_adding_stock():
    inventory = Inventory()
    inventory.add_stock("pen", 10)

    assert inventory.stock["pen"] == 10


def test_removing_stock():
    inventory = Inventory()
    inventory.add_stock("pen", 10)
    inventory.remove_stock("pen", 3)

    assert inventory.stock["pen"] == 7


def test_removing_more_stock_than_available():
    inventory = Inventory()
    inventory.add_stock("pen", 2)

    with pytest.raises(ValueError, match="^not enough stock$"):
        inventory.remove_stock("pen", 3)