def test_get_token_or_auth_user(http, base_url):
    """Проверяем, что запрос Get Token/Auth User возвращает валидный JSON."""
    r = http.get(base_url)
    assert r.status_code == 200, f"Auth endpoint failed: {r.status_code} {r.text}"
    data = r.json()
    assert data, "Empty response"
