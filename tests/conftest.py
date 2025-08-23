import pytest

from src.utils import Category, Product


@pytest.fixture
def test_category():
    return Category("Fruits", "Fresh and cheap fruits", ["apples", "bananas", "oranges"])


@pytest.fixture
def test_product():
    return Product("Apples", "Juicy golden apples", 67.9, 90)
