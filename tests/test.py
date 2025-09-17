import pytest
from src.utils import *


def test_empty_file():
    with pytest.raises(FileNotFoundError):
        read_json('non_exist_path')

def test_read_json():
    assert read_json(r'C:\Users\Thunderobot\PycharmProjects\Homework_14.1\data\test_products.json') == [
  {
    "name": "Смартфоны",
    "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
    "products": [
      {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      },
      {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
      },
      {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
      }
    ]
  }
]


def test_create_objects_from_json():
    """Тестирует основную функциональность create_objects_from_json."""

    SAMPLE_JSON_DATA = [
        {
            "name": "Electronics",
            "description": "",
            "products": [
                {
                    "name": "Laptop",
                    "description": "",
                    "price": 1200.0,
                    "quantity": 5
                },
                {
                    "name": "Keyboard",
                    "description": "",
                    "price": 75.0,
                    "quantity": 10
                }
            ]
        },
        {
            "name": "Books",
            "description": "",
            "products": [
                {
                    "name": "The Hitchhiker's Guide to the Galaxy",
                    "description": "",
                    "price": 15.5,
                    "quantity": 20
                },
                {
                    "name": "Pride and Prejudice",
                    "description": "",
                    "price": 12.0,
                    "quantity": 15
                }

            ]
        }
    ]
    objects = create_objects_from_json(SAMPLE_JSON_DATA)

    # Проверяем количество созданных объектов Category
    assert len(objects) == 2

    # Проверяем данные в первом объекте Category
    assert objects[0].name == "Electronics"
    assert len(objects[0].products) == 2
    assert objects[0].products[0] == Product(name="Laptop", price=1200.0, quantity=5, description="")
    assert objects[0].products[1] == Product(name="Keyboard", price=75.0, quantity=10, description="")

    # Проверяем данные во втором объекте Category
    assert objects[1].name == "Books"
    assert len(objects[1].products) == 2
    assert objects[1].products[0] == Product(name="The Hitchhiker's Guide to the Galaxy", price=15.5, quantity=20, description="")
    assert objects[1].products[1] == Product(name="Pride and Prejudice", price=12.0, quantity=15, description="")