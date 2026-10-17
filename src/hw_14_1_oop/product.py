from .base_container import BaseContainer
from .base_product import BaseProduct
from .mixin import LoggerMixin


class Product(LoggerMixin, BaseProduct):
    """Класс продукта для e-commerce."""

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self._price = float(price)
        self.quantity = quantity

    def __str__(self) -> str:
        """Строковое представление продукта."""
        return f"{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Сложение продуктов: цена × количество."""
        if type(self) is not type(other):
            raise TypeError("Можно складывать только товары одного класса")
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(
        cls, name: str, description: str, price: float, quantity: int
    ) -> "Product":
        """Фабричный метод для создания продукта."""
        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Геттер для цены."""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для цены с проверкой типа."""
        if isinstance(value, (int, float)):
            if value <= 0:
                raise ValueError("Цена не должна быть нулевая или отрицательная")
            self._price = float(value)
        else:
            raise TypeError("Цена должна быть числом")


class Category(BaseContainer):
    """Класс категории товаров."""

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Добавляет продукт и увеличивает счётчик."""
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты Product или его наследников"
            )
        self.__products.append(product)
        Category.product_count += 1

    def __str__(self) -> str:
        """Строковое представление категории."""
        total = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total} шт."

    def get_total(self) -> float:
        """Общее количество товаров в категории."""
        return sum(p.quantity for p in self.__products)

    def average_price(self) -> float:
        """Подсчитывает средний ценник всех товаров в категории."""
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0

    @property
    def products(self) -> str:
        """Геттер: возвращает строку со списком продуктов."""
        result = ""
        for product in self.__products:
            result += (
                f"{product.name}, {product.price} руб. "
                f"Остаток: {product.quantity} шт.\n"
            )
        return result


class Smartphone(Product):
    """Класс смартфона."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс газонной травы."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Order(BaseContainer):
    """Класс заказа: один товар, количество, итоговая стоимость."""

    def __init__(
        self,
        product: Product,
        quantity: int,
    ) -> None:
        self.product = product
        self.quantity = quantity

    def __str__(self) -> str:
        """Строковое представление заказа."""
        total = int(self.get_total())
        return (
            f"Заказ: {self.product.name}, "
            f"{self.quantity} шт., "
            f"итого: {total} руб."
        )

    def get_total(self) -> float:
        """Итоговая стоимость заказа."""
        return self.product.price * self.quantity
