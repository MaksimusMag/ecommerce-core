from src.hw_14_1_oop.product import (
    Category,
    LawnGrass,
    Product,
    Smartphone,
)


def main():
    """Проверка базового функционала (ДЗ №3)."""
    p1 = Product("Смартфон", "Мощный смартфон", 50000.0, 10)
    print(f"Товар: {p1.name}, цена: {p1.price}")

    p1.price = 45000.0
    print(f"Новая цена: {p1.price}")

    p1.price = -100

    data = {
        "name": "Ноутбук",
        "description": "Игровой",
        "price": 99999.99,
        "quantity": 5,
    }
    p2 = Product.new_product(data)
    print(f"\nСоздан через new_product: {p2.name}, {p2.price}")

    cat = Category("Электроника", "Гаджеты", [p1])
    cat.add_product(p2)

    print(f"\nКатегория: {cat.name}")
    print(cat.products)
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")


def test_inheritance():
    """Проверка наследования и ограничений (ДЗ №4)."""
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    smartphone2 = Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        98.2,
        "15",
        512,
        "Gray space",
    )
    smartphone3 = Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий",
    )

    print("\n=== Смартфоны ===")
    for phone in [smartphone1, smartphone2, smartphone3]:
        print(f"{phone.name} | {phone.model} | {phone.memory}GB | {phone.color}")

    grass1 = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    grass2 = LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )

    print("\n=== Газонная трава ===")
    for g in [grass1, grass2]:
        print(f"{g.name} | {g.country} | {g.germination_period} | {g.color}")

    # Проверка сложения
    print("\n=== Сложение ===")
    print(f"Smartphones sum: {smartphone1 + smartphone2}")
    print(f"Grass sum: {grass1 + grass2}")

    try:
        _ = smartphone1 + grass1
    except TypeError:
        print("TypeError при сложении разных типов: ОК")

    # Проверка категории
    print("\n=== Категории ===")
    cat_smart = Category("Смартфоны", "Высокотехнологичные", [smartphone1, smartphone2])
    cat_smart.add_product(smartphone3)

    print(cat_smart.products)
    print(f"Total products: {Category.product_count}")

    try:
        cat_smart.add_product("Not a product")
    except TypeError:
        print("TypeError при добавлении не-Product: ОК")


if __name__ == "__main__":
    main()
    test_inheritance()
