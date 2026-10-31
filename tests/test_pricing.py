import pytest

from src.pricing import add_tax, apply_discount


def test_basic_discount():
    assert apply_discount(100, 10) == 90


def test_zero_percent_discount():
    assert apply_discount(100, 0) == 100


def test_100_percent_discount():
    assert apply_discount(100, 100) == 0


def test_invalid_discount_percentage():
    with pytest.raises(ValueError):
        apply_discount(100, 101)


def test_default_tax():
    assert add_tax(100) == 118