import pytest

from src.utils import Category


def test_category(test_category):
    assert test_category.name == "Fruits"
    assert test_category.description == "Fresh and cheap fruits"
    assert test_category.products == ["apples", "bananas", "oranges"]
    assert test_category.category_count == 1
    assert test_category.product_count == 3

    product = Category(test_category.name, test_category.description, test_category.products)
    expected_result = "Fruits, количество продуктов: 3 шт."
    assert str(product) == expected_result

    product = Category("Test Product", "Test Description", ["apples", "bananas", "oranges"])
    assert product.products == ["apples", "bananas", "oranges"]


def test_raises(empty_test_category):
    assert empty_test_category.middle_price() == 0

def test_empty_products():
    with pytest.raises(ValueError, match="Продукты с нулевым количеством не могут быть добавлены"):
        Category("Apples", "Juicy golden apples", )

