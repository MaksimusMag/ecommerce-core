class Product:
    """Класс продукта для e-commerce."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Строковое представление продукта."""
        return f"{self.name}, {int(self.__price)} руб. " f"Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Сложение продуктов: цена × количество."""
        if type(self) is not type(other):
            raise TypeError("Можно складывать только товары одного класса")
        return self.__price * self.quantity + other.__price * other.quantity

    @property
    def price(self) -> float:
        """Геттер для приватного атрибута цены."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для цены с валидацией."""
        if value > 0:
            self.__price = value
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        """Создаёт продукт из словаря."""
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )


class Category:
    """Класс категории товаров."""

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]):
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
