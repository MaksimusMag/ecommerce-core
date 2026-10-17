from abc import ABC, abstractmethod


class BaseContainer(ABC):
    """Абстрактный базовый класс для контейнеров (Category, Order)."""

    @abstractmethod
    def get_total(self) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
