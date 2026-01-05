import pytest
from api_example import app


@pytest.fixture
def client():
    """Provides a test client for the Flask application."""
    app.config["TESTING"] = True  # Enable testing mode
    with app.test_client() as client:
        yield client  # Provide the test client instance


def test_add_user(client):
    """Test adding a new user."""
    response = client.post("/users", json={"id": 1, "name": "Alice"})

    assert response.status_code == 201
    assert response.get_json() == {"id": 1, "name": "Alice"}


def test_get_user(client):
    """Test retrieving an existing user."""
    # First, add a user to ensure it exists
    client.post("/users", json={"id": 2, "name": "Bob"})

    # Now, retrieve the user
    response = client.get("/users/2")

    assert response.status_code == 200
    assert response.get_json() == {"id": 2, "name": "Bob"}


def test_get_user_not_found(client):
    """Test retrieving a non-existing user."""
    response = client.get("/users/999")

    assert response.status_code == 404
    assert response.get_json() == {"error": "User not found"}


def test_add_duplicate_user(client):
    """Test adding a user that already exists."""
    # First, add a user
    client.post("/users", json={"id": 3, "name": "Charlie"})

    # Try to add the same user again
    response = client.post("/users", json={"id": 3, "name": "Charlie"})

    assert response.status_code == 400
    assert response.get_json() == {"error": "User already exists"}
