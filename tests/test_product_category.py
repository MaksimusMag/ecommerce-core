from src.hw_14_1_oop.product import Product, Category


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
    assert len(category.products) == 1
    assert isinstance(category.products[0], Product)


def test_category_counts_auto_increment():
    Category.category_count = 0
    Category.product_count = 0

    cat1 = Category("Категория 1", "Описание 1", [Product("Товар 1", "Опис", 100, 5)])
    cat2 = Category("Категория 2", "Описание 2",
                    [Product("Товар 2", "Опис", 200, 3), Product("Товар 3", "Опис", 300, 7)])

    assert Category.category_count == 2
    assert Category.product_count == 3
    assert cat1 is not None  # чтобы flake8 не ругался на неиспользуемую переменную
    assert cat2 is not None
