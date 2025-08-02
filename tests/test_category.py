def test_category(test_category):
    assert test_category.name == "Fruits"
    assert test_category.description == "Fresh and cheap fruits"
    assert test_category.products == ["apples", "bananas", "oranges"]
    assert test_category.category_count == 1
    assert test_category.product_count == 3
