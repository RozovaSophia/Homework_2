import pytest

from src.utils import Product, Category
from tests.conftest import TestMixinCLass


def test_products(test_product):
    assert test_product.name == "Apples"
    assert test_product.description == "Juicy golden apples"
    assert test_product.price == 67.9
    assert test_product.quantity == 90

    product = Product(test_product.name, test_product.description, test_product.price, test_product.quantity)
    expected_result = "Apples, 67.9 руб. Остаток: 90 шт."
    assert str(product) == expected_result

    product_1 = Product("Apples", "Juicy golden apples", 67.9, 90)
    result = product_1.price * product_1.quantity
    assert result == 6111.000000000001

    product_1 = Product("Apples", "Juicy golden apples", 67.9, 90)
    product_2 = Product("Bananas", "Juicy yellow Bananas", 78.8, 80)
    result = product_1.price * product_1.quantity + product_2.price * product_2.quantity
    assert result == 12415.0

    product = Product("Test Product", "Test Description", 150.0, 7)
    assert product.price == 150.0

    product = Product("Test Product", "Test Description", 150.0, 7)
    product.price = 200.0
    assert product.price == 200.0


def test_empty_product():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Apples", "Juicy golden apples", 100, 0)

def test_mixin_method():
    result = TestMixinCLass("Name", "Description", 0, 0)
    assert result.name == "Name"
    assert result.description == "Description"
    assert result.price == 0
    assert result.quantity == 0

def test_add_method():
    product_1 = Product("Apples", "Juicy golden apples", 100, 2)
    product_2 = Product("Bananas", "Juicy yellow Bananas", 50, 4)
    expected_result = (100 * 2) + (50 * 4)
    assert product_1 + product_2 == expected_result

    product_3 = ("Fruits", "Fresh and cheap fruits", 2, 5)
    assert product_1 + product_3 is None