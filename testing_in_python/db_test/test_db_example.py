import pytest
from db_example import Database, save_user_to_db


@pytest.fixture
def db():
    """Provides a fresh instance of the Database class and cleans up after the test."""
    db_instance = Database()
    yield db_instance  # Provide the fixture instance
    db_instance.data.clear()  # Cleanup after test (not needed for in-memory, but useful for real DBs)


def test_add_user(db):
    db.add_user(1, "Alice")
    assert db.get_user(1) == "Alice"

    db.add_user(2, "Bob")
    assert db.get_user(2) == "Bob"


def test_add_duplicate_user(db):
    db.add_user(1, "Alice")
    with pytest.raises(ValueError) as excinfo:
        db.add_user(1, "Bob")
    assert str(excinfo.value) == "User ID already exists."


def test_delete_user(db):
    db.add_user(1, "Alice")
    db.delete_user(1)
    assert db.get_user(1) is None


def test_delete_nonexistent_user(db):
    with pytest.raises(ValueError) as excinfo:
        db.delete_user(1)
    assert str(excinfo.value) == "User ID does not exist."


def test_save_user_to_db(mocker):
    mock_conn = mocker.patch("sqlite3.connect")
    mock_cursor = mock_conn.return_value.cursor.return_value

    save_user_to_db("Charlie", 30)

    mock_conn.assert_called_once_with("users.db")
    mock_cursor.execute_called_once_with(
        "INSERT INTO users (name, age) VALUES (?, ?)", ("Charlie", 30)
    )
