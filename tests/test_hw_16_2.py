import pytest

from src.hw_14_1_oop.base_container import BaseContainer
from src.hw_14_1_oop.base_product import BaseProduct
from src.hw_14_1_oop.mixin import LoggerMixin
from src.hw_14_1_oop.product import Category, LawnGrass, Order, Product, Smartphone


class TestBaseProduct:
    """Тесты абстрактного класса BaseProduct."""

    def test_base_product_is_abstract(self):
        """BaseProduct нельзя инстанциировать напрямую."""
        with pytest.raises(TypeError):
            BaseProduct("Test", "Desc", 100, 1)

    def test_product_inherits_base_product(self):
        """Product наследуется от BaseProduct."""
        assert issubclass(Product, BaseProduct)

    def test_product_has_price_property(self):
        """У Product есть property price из BaseProduct."""
        product = Product("Test", "Desc", 150.0, 5)
        assert product.price == 150.0

    def test_product_price_setter_valid(self):
        """Сеттер price принимает положительное значение."""
        product = Product("Test", "Desc", 100.0, 1)
        product.price = 200.0
        assert product.price == 200.0

    def test_product_price_setter_invalid(self):
        """Сеттер price отклоняет неположительные значения."""
        product = Product("Test", "Desc", 100.0, 1)
        product.price = -50.0
        assert product.price == 100.0  # Цена не изменилась

    def test_new_product_classmethod(self):
        """Classmethod new_product создаёт продукт из словаря."""
        data = {
            "name": "iPhone",
            "description": "Phone",
            "price": 999.0,
            "quantity": 10,
        }
        product = Product.new_product(data)
        assert isinstance(product, Product)
        assert product.name == "iPhone"
        assert product.price == 999.0


class TestLoggerMixin:
    """Тесты миксина LoggerMixin."""

    def test_mixin_logs_product_creation(self, capsys):
        """Миксин печатает информацию о создании Product."""
        Product("TestProd", "Desc", 1200.0, 10)
        captured = capsys.readouterr()
        assert "Product(" in captured.out
        assert "'TestProd'" in captured.out
        assert "1200.0" in captured.out

    def test_mixin_logs_smartphone_creation(self, capsys):
        """Миксин печатает информацию о создании Smartphone."""
        Smartphone("S24", "Flagship", 89900.0, 5, 0.95, "S24 Ultra", 256, "black")
        captured = capsys.readouterr()
        assert "Smartphone(" in captured.out
        assert "'S24'" in captured.out

    def test_mixin_logs_lawn_grass_creation(self, capsys):
        """Миксин печатает информацию о создании LawnGrass."""
        LawnGrass("GreenMix", "Lawn", 500.0, 20, "Russia", "7-14 days", "green")
        captured = capsys.readouterr()
        assert "LawnGrass(" in captured.out
        assert "'GreenMix'" in captured.out


class TestOrder:
    """Тесты класса Order."""

    def setup_method(self):
        """Создаём тестовый продукт для заказов."""
        self.product = Product("Laptop", "PC", 50000.0, 3)

    def test_order_creation(self):
        """Заказ создаётся с товаром и количеством."""
        order = Order(self.product, 2)
        assert order.product == self.product
        assert order.quantity == 2

    def test_order_get_total(self):
        """get_total возвращает цену × количество."""
        order = Order(self.product, 3)
        assert order.get_total() == 150000.0

    def test_order_str(self):
        """__str__ возвращает читаемое представление заказа."""
        order = Order(self.product, 2)
        result = str(order)
        assert "Laptop" in result
        assert "2 шт." in result
        assert "100000 руб." in result

    def test_order_inherits_base_container(self):
        """Order наследуется от BaseContainer."""
        assert issubclass(Order, BaseContainer)


class TestCategoryBaseContainer:
    """Тесты Category как наследника BaseContainer."""

    def test_category_inherits_base_container(self):
        """Category наследуется от BaseContainer."""
        assert issubclass(Category, BaseContainer)

    def test_category_get_total(self):
        """get_total возвращает общее количество товаров."""
        p1 = Product("A", "Desc", 100.0, 5)
        p2 = Product("B", "Desc", 200.0, 3)
        category = Category("Tech", "Electronics", [p1, p2])
        assert category.get_total() == 8


class TestMRO:
    """Тесты корректности MRO."""

    def test_product_mro(self):
        """MRO Product включает LoggerMixin и BaseProduct."""
        mro_names = [cls.__name__ for cls in Product.__mro__]
        assert "LoggerMixin" in mro_names
        assert "BaseProduct" in mro_names
        # LoggerMixin должен быть перед BaseProduct
        assert mro_names.index("LoggerMixin") < mro_names.index("BaseProduct")

    def test_smartphone_inherits_all(self):
        """Smartphone наследует всю цепочку."""
        assert issubclass(Smartphone, Product)
        assert issubclass(Smartphone, BaseProduct)
        assert issubclass(Smartphone, LoggerMixin)
