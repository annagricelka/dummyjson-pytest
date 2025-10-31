def test_get_all_products(http, base_url):
    """Проверяем, что Get All Products возвращает список товаров или JSON."""
    r = http.get(base_url)
    assert r.status_code == 200, f"Products endpoint failed: {r.status_code} {r.text}"

    data = r.json()
    assert data, "Response is empty"
