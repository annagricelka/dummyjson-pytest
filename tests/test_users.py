def test_users_endpoint_returns_data(http, base_url):
    """Проверяем, что эндпоинт возвращает список пользователей/продавцов."""
    r = http.get(base_url)
    assert r.status_code == 200, f"Unexpected status: {r.status_code} {r.text}"

    data = r.json()
    assert isinstance(data, (list, dict)), f"Unexpected type: {type(data)}"
    assert len(data) > 0, "Response is empty"

    # Если это список объектов с email
    if isinstance(data, list):
        emails = [u.get("email") for u in data if isinstance(u, dict) and "email" in u]
        if emails:
            assert any("@" in e for e in emails), "Emails seem invalid"
