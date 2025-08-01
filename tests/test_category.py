def test_category(test_category):
    assert test_category.name == 'Fruits'
    assert test_category.description == 'Fresh and cheap fruits'
    assert test_category.products == ['apples', 'bananas', 'oranges']
    assert test_category.count_category == 1

