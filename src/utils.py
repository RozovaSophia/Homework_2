import json
import os
from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Mixin:

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.name} {self.price} {self.quantity} {self.description}"


class Product(BaseProduct, Mixin):
    """инициализирует свойства продукта, умножает количество продукта на его стоимость"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        if quantity != 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.description = description
        self.name = name
        self.__price = price

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __mul__(self, other):
        return self.__price * other.quantity

    def __add__(self, other):
        try:
            if isinstance(other, Product):
                return (self.__price * self.quantity) + (other.__price * other.quantity)
            else:
                raise TypeError
        except TypeError:
            print("Ошибка типа данных")
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
        if products is not None:
            self.__products = products
        else:
            raise ValueError("Продукты с нулевым количеством не могут быть добавлены")
        Category.category_count += 1
        Category.product_count = len(self.__products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {Category.product_count} шт."

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1

    def middle_price(self):
        try:
            total_price = 0
            for product in self.__products:
                total_price += product.price
            middle_price = total_price / Category.product_count
        except ZeroDivisionError as e:
            return f"{e}"
        else:
            return middle_price

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


if __name__ == "__main__":
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством"
        )
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
