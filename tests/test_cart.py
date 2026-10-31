from src.cart import Cart


def test_adding_products_and_calculating_total_with_discount():
    cart = Cart()
    cart.add("pen", 50, 2)

    assert cart.total(10) == 106.2


def test_empty_cart_total():
    assert Cart().total() == 0