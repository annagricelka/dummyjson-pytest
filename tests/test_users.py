# tests/test_users.py

import requests


def test_users_contains_emily(base_url):
    """
    1. GET /users
    2. Проверить, что в списке есть пользователь с нужным email.
    """
    response = requests.get(f"{base_url}/users")
    assert response.status_code == 200, "Ожидаем статус 200 для /users"

    data = response.json()
    users = data.get("users", [])

    # проверяем, что список вообще не пустой
    assert users, "Список users пустой"

    target_email = "emily.johnson@x.dummyjson.com"
    emails = [user.get("email") for user in users]

    assert target_email in emails, (
        f"Пользователь с email {target_email} не найден в ответе /users"
    )
