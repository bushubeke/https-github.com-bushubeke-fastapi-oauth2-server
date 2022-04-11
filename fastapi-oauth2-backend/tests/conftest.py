import pytest
from fastapi.testclient import TestClient
from oauth2.main import create_dev_app


app=create_dev_app()

@pytest.fixture(scope="module")
def testing_client():
    yield  TestClient(app)
