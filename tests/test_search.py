import pytest

@pytest.mark.parametrize("query", ["apple", "banana", "pear", "vodka", "coffee"])
def test_search_products(http, base_url, query):
    """Проверяем поиск (Search Products)."""
    url = base_url  # пока тот же URL, если добавится query, можно добавить params={"q": query}
    r = http.get(url)
    assert r.status_code == 200, f"Search failed for {query}: {r.status_code}"
    assert r.json(), f"Empty response for query {query}"
