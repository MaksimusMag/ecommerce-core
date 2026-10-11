import pytest

from src.hw_14_1_oop.product import (
    Category,
    LawnGrass,
    Product,
    Smartphone,
)


def test_product_initialization():
    product = Product("Ноутбук", "Мощный игровой", 99999.99, 10)
    assert product.name == "Ноутбук"
    assert product.description == "Мощный игровой"
    assert product.price == 99999.99
    assert product.quantity == 10


def test_category_initialization():
    products = [Product("Мышь", "Беспроводная", 2500.0, 50)]
    category = Category("Периферия", "Компьютерные мыши", products)

    assert category.name == "Периферия"
    assert category.description == "Компьютерные мыши"
    assert "Мышь" in category.products
    assert "2500.0 руб." in category.products
    assert "Остаток: 50 шт." in category.products


def test_category_counts_auto_increment():
    Category.category_count = 0
    Category.product_count = 0

    cat1 = Category("Категория 1", "Описание 1", [Product("Товар 1", "Опис", 100, 5)])
    cat2 = Category(
        "Категория 2",
        "Описание 2",
        [Product("Товар 2", "Опис", 200, 3), Product("Товар 3", "Опис", 300, 7)],
    )

    assert Category.category_count == 2
    assert Category.product_count == 3
    assert cat1 is not None
    assert cat2 is not None


def test_add_product():
    Category.category_count = 0
    Category.product_count = 0

    cat = Category("Тест", "Описание", [])
    p = Product("Товар", "Опис", 100, 5)
    cat.add_product(p)

    assert "Товар" in cat.products
    assert Category.product_count == 1


def test_price_getter():
    p = Product("Тест", "Опис", 500.0, 10)
    assert p.price == 500.0


def test_price_setter_valid():
    p = Product("Тест", "Опис", 100.0, 5)
    p.price = 200.0
    assert p.price == 200.0


def test_price_setter_invalid(capsys):
    p = Product("Тест", "Опис", 100.0, 5)
    p.price = -50
    captured = capsys.readouterr()
    msg = "Цена не должна быть нулевая или отрицательная"
    assert msg in captured.out
    assert p.price == 100.0


def test_new_product():
    data = {
        "name": "Телефон",
        "description": "Смартфон",
        "price": 30000.0,
        "quantity": 20,
    }
    p = Product.new_product(data)

    assert p.name == "Телефон"
    assert p.description == "Смартфон"
    assert p.price == 30000.0
    assert p.quantity == 20


def test_products_getter_format():
    p1 = Product("Товар1", "Опис1", 100.0, 5)
    p2 = Product("Товар2", "Опис2", 200.0, 10)
    cat = Category("Тест", "Описание", [p1, p2])

    expected = (
        "Товар1, 100.0 руб. Остаток: 5 шт.\n" "Товар2, 200.0 руб. " "Остаток: 10 шт.\n"
    )
    assert cat.products == expected


def test_product_str():
    p = Product("Samsung Galaxy", "256GB", 180000.0, 5)
    assert str(p) == "Samsung Galaxy, 180000 руб. Остаток: 5 шт."


def test_category_str():
    products = [
        Product("Товар1", "Опис", 100.0, 5),
        Product("Товар2", "Опис", 200.0, 10),
    ]
    cat = Category("Электроника", "Гаджеты", products)
    assert str(cat) == "Электроника, количество продуктов: 15 шт."


def test_product_add():
    p1 = Product("A", "Опис", 100.0, 10)
    p2 = Product("B", "Опис", 200.0, 2)
    assert p1 + p2 == 1400.0


def test_smartphone_creation():
    """Тест создания смартфона."""
    phone = Smartphone(
        name="iPhone",
        description="Смартфон Apple",
        price=99999.0,
        quantity=5,
        efficiency=9.5,
        model="15 Pro",
        memory=256,
        color="Titanium",
    )
    assert phone.name == "iPhone"
    assert phone.efficiency == 9.5
    assert phone.model == "15 Pro"
    assert phone.memory == 256
    assert phone.color == "Titanium"


def test_lawn_grass_creation():
    """Тест создания газонной травы."""
    grass = LawnGrass(
        name="Газонная трава",
        description="Для дачи",
        price=500.0,
        quantity=100,
        country="Россия",
        germination_period="7 дней",
        color="Зелёный",
    )
    assert grass.name == "Газонная трава"
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зелёный"


def test_add_same_type_products():
    """Тест сложения продуктов одного типа."""
    p1 = Product("A", "Опис", 100.0, 10)
    p2 = Product("B", "Опис", 200.0, 5)
    assert p1 + p2 == 2000.0


def test_add_different_types_raises_error():
    """Тест ошибки при сложении разных типов."""
    phone = Smartphone(
        name="Phone",
        description="Desc",
        price=1000.0,
        quantity=1,
        efficiency=8.0,
        model="X",
        memory=128,
        color="Black",
    )
    grass = LawnGrass(
        name="Grass",
        description="Desc",
        price=100.0,
        quantity=1,
        country="RU",
        germination_period="5 days",
        color="Green",
    )
    with pytest.raises(TypeError):
        phone + grass


def test_add_product_invalid_type():
    """Тест ошибки при добавлении не-Product объекта."""
    cat = Category("Test", "Desc", [])
    with pytest.raises(TypeError):
        cat.add_product("Не продукт")
