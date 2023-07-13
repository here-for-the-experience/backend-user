import pytest
from fastapi.testclient import TestClient
from fastapi import status
from ..main import app

client = TestClient(app)
ENDPOINT = "http://127.0.0.1:8000"

@pytest.mark.parametrize(
    "path,method",
    [
        (f"{ENDPOINT}/users/create", "POST"),
        (f"{ENDPOINT}/users/update", "PUT"),
        (f"{ENDPOINT}/users/profile", "GET"),
        (f"{ENDPOINT}/users/forgot", "POST"),
        (f"{ENDPOINT}/users/validate", "POST"),
        (f"{ENDPOINT}/login", "POST"),
        (f"{ENDPOINT}/users/city", "GET"),

        
    ],
)
def test_route_exists(path: str, method: str) -> None:
    """
    Test if the specified route exists and is reachable.
    """
    response = client.request(method, path)
    assert response.status_code not in (
        status.HTTP_404_NOT_FOUND,
        status.HTTP_405_METHOD_NOT_ALLOWED,
    )