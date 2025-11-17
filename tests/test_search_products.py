# tests/test_search_products.py

import requests
import pytest

# Берём базовый URL напрямую, чтобы на этапе импорта модуля получить продукты
BASE_URL = "https://dummyjson.com"


def _get_product_titles(limit=5):
    """
    Вспомогательная функция:
    1. Делает GET /products
    2. Берёт первые N (limit) продуктов
    3. Возвращает список их title
    """
    response = requests.get(f"{BASE_URL}/products")
    response.raise_for_status()

    data = response.json()
    products = data.get("products", [])

    titles = [p.get("title") for p in products if p.get("title")]
    # На всякий случай обрежем до нужного количества
    return titles[:limit]


# Здесь формируется список строк для параметризации —
# по сути, 5 разных продуктов "из прошлого шага".
SEARCH_QUERIES = _get_product_titles(limit=5)


@pytest.mark.parametrize("query", SEARCH_QUERIES)
def test_search_products_returns_results(base_url, query):
    """
    Для каждого значения q (название продукта):
    1. GET /products/search?q=<query>
    2. Проверить, что вернулся хотя бы один продукт.
    3. У найденных продуктов есть title, description, price.
    4. Среди найденных есть хотя бы один продукт с таким же title.
    """
    response = requests.get(f"{base_url}/products/search", params={"q": query})
    assert response.status_code == 200, (
        f"Ожидаем статус 200 для /products/search?q={query}"
    )

    data = response.json()
    products = data.get("products", [])

    assert len(products) >= 1, (
        f"По запросу '{query}' не найдено ни одного продукта"
    )

    # Проверяем поля у продуктов
    for product in products:
        assert "price" in product, "У продукта нет поля 'price'"
        assert product["price"] is not None, "Поле 'price' = None"

        assert "title" in product, "У продукта нет поля 'title'"
        assert product["title"], "Поле 'title' пустое"

        assert "description" in product, "У продукта нет поля 'description'"
        assert product["description"], "Поле 'description' пустое"

    # Дополнительно: убеждаемся, что среди результатов поиска есть продукт
    # с точно таким же названием, как мы искали.
    titles = [p.get("title") for p in products]
    assert query in titles, (
        f"Среди результатов поиска по '{query}' нет продукта с title == '{query}'"
    )
