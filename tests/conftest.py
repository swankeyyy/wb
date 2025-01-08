import pytest_asyncio
from app.main import app

from fastapi.testclient import TestClient


# @pytest.fixture(scope="session")
# def event_loop():
#     loop = asyncio.get_event_loop_policy().new_event_loop()
#     yield loop
#     loop.close()


@pytest_asyncio.fixture(scope="session", autouse=False)
def client():
    """fixture for client testing"""
    with TestClient(app) as client:
        yield client
    client.close()