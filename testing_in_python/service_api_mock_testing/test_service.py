import pytest
from service import APIClient, UserService


def test_get_username_with_mock(mocker):
    mock_api_client = mocker.Mock(spec=APIClient)  # Create a mock APIClient

    mock_api_client.get_user_data.return_value = {"id": 1, "name": "John Doe"}

    service = UserService(api_client=mock_api_client)  # Inject mock API client

    result = service.get_username(user_id=1)

    assert result == "JOHN DOE"  # Verify the processed result
    mock_api_client.get_user_data.assert_called_once_with(1)  # Ensure correct API call
