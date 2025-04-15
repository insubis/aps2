import pytest
import requests
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    return "https://reqres.in/api"  # Certifique-se que tem http/https

@pytest.fixture
def headers():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

@pytest.fixture
def session(base_url, headers):
    session = requests.Session()
    session.headers.update(headers)
    
    # Garantir que a base_url termine com /
    if not base_url.endswith('/'):
        base_url = base_url + '/'
    
    session.base_url = base_url
    yield session
    session.close()