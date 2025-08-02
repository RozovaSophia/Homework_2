import json
import os


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count = len(products) if products else 0


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as f:
        data = json.load(f)
    return data


def create_objects_from_json(data):
    objects = []
    for item in data:
        products = []

        for product in item["products"]:
            products.append(Product(**product))

        item["products"] = products
        objects.append(Category(**item))

    return objects


if __name__ == "__main__":
    result = create_objects_from_json(read_json("../data/products.json"))
    print(result)
