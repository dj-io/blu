import pytest
from unittest.mock import patch
import os
import questionary
from blu.utils.directories import detect_directory


# Mock config objects
@pytest.fixture
def mock_config_with_cached_directories():
    return {"cached_directories": ["/path/to/project1", "/path/to/project2"]}


@pytest.fixture
def mock_config_without_cached_directories():
    return {"cached_directories": []}


@patch("blu.utils.directories.detect_directory", return_value="/detected/path")
@patch("questionary.select")
@patch("os.getcwd", return_value="/current/dir")
def test_cached_directories_with_choices(
    mock_getcwd,
    mock_questionary_select,
    mock_detect_directory,
    mock_config_with_cached_directories,
):
    """
    Test behavior when cached_directories is populated.
    """
    # Arrange
    mock_questionary_select.return_value.ask.return_value = "/path/to/project1"

    config = mock_config_with_cached_directories
    choices = config["cached_directories"] + [
        "Use Current Directory",
        "Use Different Directory",
    ]
    directory_choice = questionary.select("Select a directory:", choices=choices).ask()

    # Act
    if directory_choice == "Use Current Directory":
        parent_dir = os.getcwd()
    elif directory_choice == "Use Different Directory":
        parent_dir = detect_directory()
    else:
        parent_dir = directory_choice

    # Assert
    mock_questionary_select.assert_called_once_with(
        "Select a directory:", choices=choices
    )
    assert parent_dir == "/path/to/project1"
