from src.hw_14_1_oop.product import Product, Category


def main():
    p1 = Product(
        "Смартфон", "Мощный смартфон", 50000.0, 10
    )
    print(f"Товар: {p1.name}, цена: {p1.price}")

    p1.price = 45000.0
    print(f"Новая цена: {p1.price}")

    p1.price = -100

    data = {
        "name": "Ноутбук",
        "description": "Игровой",
        "price": 99999.99,
        "quantity": 5
    }
    p2 = Product.new_product(data)
    print(f"\nСоздан через new_product: {p2.name}, {p2.price}")

    cat = Category("Электроника", "Гаджеты", [p1])
    cat.add_product(p2)

    print(f"\nКатегория: {cat.name}")
    print(cat.products)
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")


if __name__ == "__main__":
    main()
