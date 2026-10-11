class LoggerMixin:
    """Миксин для логирования создания объектов через __repr__."""

    def __init__(self, *args, **kwargs) -> None:
        class_name = self.__class__.__name__

        # Формируем строку логирования ВСЕХ параметров
        args_repr = ", ".join(repr(arg) for arg in args)
        kwargs_repr = ", ".join(f"{key}={repr(value)}" for key, value in kwargs.items())
        params = ", ".join(filter(None, [args_repr, kwargs_repr]))
        print(f"{class_name}({params})")

        # Передаём ТОЛЬКО те kwargs, которые нужны базовому классу
        # (BaseProduct принимает только name, description, price, quantity)
        base_kwargs = {
            k: v
            for k, v in kwargs.items()
            if k in ("name", "description", "price", "quantity")
        }
        super().__init__(*args, **base_kwargs)
