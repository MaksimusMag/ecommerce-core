from src.hw_14_1_oop.product import Product, Category


def main():
    products = [
        Product("Смартфон", "Мощный смартфон", 50000.0, 10),
        Product("Чехол", "Защитный чехол", 1000.0, 50)
    ]
    category = Category("Электроника", "Гаджеты и аксессуары", products)

    print(f"Категория: {category.name}")
    print(f"Товаров в категории: {len(category.products)}")
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")


if __name__ == "__main__":
    main()
