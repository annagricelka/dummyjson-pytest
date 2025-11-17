# tests/test_products.py

import requests


def test_products_have_required_fields(base_url):
    """
    1. GET /products
    2. Проверить, что вернулось минимум 5 продуктов.
    3. Для каждого продукта есть price, title, description (и они не пустые).
    """
    response = requests.get(f"{base_url}/products")
    assert response.status_code == 200, "Ожидаем статус 200 для /products"

    data = response.json()
    products = data.get("products", [])

    assert len(products) >= 5, (
        f"Ожидалось минимум 5 продуктов, а пришло {len(products)}"
    )

    for product in products:
        assert "price" in product, "У продукта нет поля 'price'"
        assert product["price"] is not None, "Поле 'price' = None"

        assert "title" in product, "У продукта нет поля 'title'"
        assert product["title"], "Поле 'title' пустое"

        assert "description" in product, "У продукта нет поля 'description'"
        assert product["description"], "Поле 'description' пустое"
