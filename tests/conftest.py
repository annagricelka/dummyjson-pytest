import os
import pytest
import requests
from dotenv import load_dotenv

# Подгружаем переменные из .env (если есть)
load_dotenv()

# Твой API-эндпоинт
BASE_URL = os.getenv("BASE_URL", "http://dashboard-bm-eu-stage1.bidmachine.io/api/sellers/json")

@pytest.fixture(scope="session")
def base_url():
    """Базовый URL API"""
    return BASE_URL

@pytest.fixture(scope="session")
def http():
    """HTTP-сессия для всех запросов"""
    s = requests.Session()
    s.headers.update({"Accept": "application/json"})
    return s
