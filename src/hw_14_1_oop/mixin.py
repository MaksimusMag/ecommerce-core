import logging


class LoggerMixin:
    """Миксин для логгирования событий."""

    def log(self, message: str) -> None:
        logging.info(f"{self.__class__.__name__}: {message}")
