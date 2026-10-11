from .base_container import BaseContainer
from .base_product import BaseProduct
from .mixin import LoggerMixin


class Product(LoggerMixin, BaseProduct):
    """Класс продукта для e-commerce."""

    def __str__(self) -> str:
        """Строковое представление продукта."""
        return f"{self.name}, {int(self.price)} руб. " f"Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Сложение продуктов: цена × количество."""
        if type(self) is not type(other):
            raise TypeError("Можно складывать только товары одного класса")
        return self.price * self.quantity + other.price * other.quantity


class Category(BaseContainer):
    """Класс категории товаров."""

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.__products: list[Product] = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Добавляет продукт и увеличивает счётчик."""
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты Product " "или его наследников"
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
        super().__init__(
            name,
            description,
            price,
            quantity,
            efficiency=efficiency,
            model=model,
            memory=memory,
            color=color,
        )
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
        super().__init__(
            name,
            description,
            price,
            quantity,
            country=country,
            germination_period=germination_period,
            color=color,
        )
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
