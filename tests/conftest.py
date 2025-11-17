# tests/conftest.py

import pytest
import requests

BASE_URL = "https://dummyjson.com"


@pytest.fixture(scope="session")
def base_url():
    """Базовый URL для всех запросов."""
    return BASE_URL


@pytest.fixture(scope="session")
def auth_token(base_url):
    """
    Логинится на /auth/login и возвращает accessToken.
    Используем пользователя из документации DummyJSON.
    """
    login_payload = {
        "username": "emilys",
        "password": "emilyspass",
        # "expiresInMins": 30  # можно добавить, но не обязательно
    }

    response = requests.post(f"{base_url}/auth/login", json=login_payload)
    # если код не 2xx — выбросит исключение и сразу покажет ошибку
    response.raise_for_status()

    data = response.json()
    token = data.get("accessToken")

    assert token, "В ответе на /auth/login нет accessToken"

    return token


@pytest.fixture
def auth_headers(auth_token):
    """
    Заголовки с Authorization для запросов,
    где нужна авторизация.
    """
    return {
        "Authorization": f"Bearer {auth_token}"
    }
