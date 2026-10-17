from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов."""

    @abstractmethod
    def __str__(self) -> str:
        pass

    @classmethod
    @abstractmethod
    def new_product(
        cls, name: str, description: str, price: float, quantity: int
    ) -> "BaseProduct":
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass
