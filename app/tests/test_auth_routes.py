import pytest
from fastapi.testclient import TestClient
from fastapi import status
from ..main import app

client = TestClient(app)
ENDPOINT = "http://127.0.0.1:8000"

@pytest.mark.parametrize(
    "path,method",
    [
        (f"{ENDPOINT}/create", "POST"),
        # (f"{ENDPOINT}/update", "PUT"),
        (f"{ENDPOINT}/profile", "GET"),
        (f"{ENDPOINT}/forgot", "POST"),
        (f"{ENDPOINT}/validate", "POST"),
        (f"{ENDPOINT}/login", "POST"),

        
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