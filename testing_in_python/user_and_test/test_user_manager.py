import pytest
from user_manager import UserManager


@pytest.fixture
def user_manager():
    """Creates a fresh UserManager instance for each test."""
    return UserManager()


def test_add_user(user_manager):
    assert user_manager.add_user("alice", "alice@example.com") is True
    assert user_manager.get_user("alice") == "alice@example.com"


def test_add_duplicate_user(user_manager):
    user_manager.add_user("alice", "alice@example.com")
    with pytest.raises(ValueError, match="User already exists"):
        user_manager.add_user("alice", "alice2@example.com")
