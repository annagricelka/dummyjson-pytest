# tests/test_auth.py

import requests


def test_login_and_get_auth_user(base_url):
    """
    1. POST /auth/login -> получить токен и данные юзера.
    2. GET /auth/me с Authorization: Bearer <token>.
    3. Проверить, что email и username совпадают.
    """
    login_payload = {
        "username": "emilys",
        "password": "emilyspass",
    }

    # Шаг 1: логинимся
    login_response = requests.post(f"{base_url}/auth/login", json=login_payload)
    assert login_response.status_code == 200, "Ожидаем статус 200 для /auth/login"

    login_data = login_response.json()
    access_token = login_data.get("accessToken")

    assert access_token, "В ответе /auth/login нет accessToken"

    # Шаг 2: получаем /auth/me
    headers = {"Authorization": f"Bearer {access_token}"}
    me_response = requests.get(f"{base_url}/auth/me", headers=headers)
    assert me_response.status_code == 200, "Ожидаем статус 200 для /auth/me"

    me_data = me_response.json()

    # Шаг 3: проверяем, что это тот же пользователь
    assert me_data.get("email") == login_data.get("email"), (
        "email в /auth/me не совпадает с email в ответе /auth/login"
    )
    assert me_data.get("username") == login_data.get("username"), (
        "username в /auth/me не совпадает с username в ответе /auth/login"
    )
