import json
import os
from abc import ABC, abstractmethod

class BaseProduct:

    @abstractmethod
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Mixin():

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name} {self.price} {self.quantity} {self.description}'


class Product(BaseProduct, Mixin):
    """инициализирует свойства продукта, умножает количество продукта на его стоимость"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __mul__(self, other):
        return self.__price * other.quantity

    def __add__(self, other):
        try:
            if type(self) == type(other):
                return (self.__price * self.quantity) + (other.__price * other.quantity)
            else:
                raise TypeError
        except TypeError:
            print('Ошибка типа данных')
            return None

    @property
    def products(self):
        return str(self)

    @classmethod
    def new_product(cls, product_data):
        if isinstance(product_data, dict):
            if issubclass(product_data, Product):
                name = product_data["name"]
                description = product_data["description"]
                price = product_data["price"]
                quantity = product_data["quantity"]
                return cls(name, description, price, quantity)
            else:
                raise TypeError
        else:
            raise TypeError

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if int(price) <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = price


class Category:
    """создает категории продуктов, считает их"""
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count = len(self.__products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {Category.product_count} шт."

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1

    @property
    def products(self):
        return self.__products


class Smartphone(Product):
    """дочерний класс, который описывает только смартфоны"""
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """дочерний класс, который описывает только газонную траву"""
    country: str
    germination_period: int
    color: str

    def __init__(self, name, description, price, quantity, country: str, germination_period: int, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


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


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)