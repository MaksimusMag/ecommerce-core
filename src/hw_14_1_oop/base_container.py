from abc import ABC, abstractmethod


class BaseContainer(ABC):
    """Абстрактный базовый класс для контейнеров (Order, Category)."""

    @abstractmethod
    def get_total(self) -> float:
        """Возвращает общую стоимость или количество."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Строковое представление контейнера."""
        pass
