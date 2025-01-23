import os
import pytest
import subprocess
import configparser
from unittest.mock import patch, MagicMock
from apollo.utils.directories import detect_directory
from apollo.utils.run_command import run_command
from apollo.utils.config import ensure_pypirc


@pytest.fixture
def mock_pypirc_file(tmp_path):
    """
    Fixture to create a temporary .pypirc file for testing.
    """
    return tmp_path / ".pypirc"


# ----------------------------------------------------------- DETECTIONS -----------------------------------------------------------------

@patch("apollo.utils.directories.os.path.exists")
@patch("apollo.utils.directories.create_directory")
@patch("apollo.utils.directories.get_subdirectories")
@patch("apollo.utils.directories.questionary")
def test_detect_directory_developer_exists(
    mock_questionary, mock_get_subdirectories, mock_create_directory, mock_path_exists
):
    """
    Test detect_directory when the Developer directory exists and is selected.
    """
    mock_path_exists.side_effect = lambda path: path.endswith("Developer")
    mock_questionary.confirm.return_value.ask.return_value = True  # Simulate user saying yes
    mock_get_subdirectories.return_value = {}  # No subdirectories in the Developer folder

    result = detect_directory()
    assert result.endswith("Developer")
    mock_path_exists.assert_called_with(os.path.expanduser("~/Developer"))
    mock_get_subdirectories.assert_called_once_with(os.path.expanduser("~/Developer"))


@patch("apollo.utils.directories.os.path.exists")
@patch("apollo.utils.directories.create_directory")
@patch("apollo.utils.directories.get_subdirectories")
@patch("apollo.utils.directories.questionary")
def test_detect_directory_create_developer(
    mock_questionary, mock_get_subdirectories, mock_create_directory, mock_path_exists
):
    """
    Test detect_directory when the Developer directory does not exist and is created.
    """
    mock_path_exists.side_effect = lambda path: False  # Developer folder doesn't exist
    mock_questionary.confirm.return_value.ask.return_value = True  # Simulate user saying yes
    mock_get_subdirectories.return_value = {}  # No subdirectories in the fallback folder

    result = detect_directory()
    assert result.endswith("Developer")
    mock_create_directory.assert_called_once_with(os.path.expanduser("~/Developer"))


@patch("apollo.utils.directories.os.path.exists")
@patch("apollo.utils.directories.create_directory")
@patch("apollo.utils.directories.get_subdirectories")
@patch("apollo.utils.directories.questionary")
def test_detect_directory_create_new_directory(
    mock_questionary, mock_get_subdirectories, mock_create_directory, mock_path_exists
):
    """
    Test detect_directory when creating a new directory is selected.
    """
    mock_path_exists.return_value = False  # Developer folder doesn't exist
    mock_get_subdirectories.side_effect = lambda path: {"sub1": os.path.join(path, "sub1")}
    mock_questionary.confirm.return_value.ask.return_value = False  # Simulate user saying no to creating Developer
    mock_questionary.select.return_value.ask.side_effect = ["Create a New Directory"]  # User selects create new dir
    mock_questionary.path.return_value.ask.return_value = "/new/path"  # New path entered by user

    result = detect_directory()
    assert result == "/new/path"
    mock_create_directory.assert_called_once_with("/new/path")
    
# ----------------------------------------------------------- RUN COMMANDS -----------------------------------------------------------------
    
@patch("apollo.utils.run_command.subprocess.run")
@patch("apollo.utils.run_command.Halo")
def test_run_command_success(mock_halo, mock_run):
    """
    Test run_command for successful command execution.
    """
    # Mock the spinner
    mock_spinner = MagicMock()
    mock_halo.return_value = mock_spinner

    # Mock subprocess.run for a successful execution
    mock_result = MagicMock()
    mock_result.stdout = "Command executed successfully."
    mock_result.returncode = 0
    mock_run.return_value = mock_result

    # Call the function
    command = "echo 'hello'"
    output = run_command(command)

    # Assertions
    mock_spinner.start.assert_called_once_with("Process")
    mock_spinner.succeed.assert_called_once_with("Process - Completed successfully.")
    mock_run.assert_called_once_with(
        command, shell=True, cwd=None, check=True, text=True, capture_output=True
    )
    assert output == "Command executed successfully."


@patch("apollo.utils.run_command.subprocess.run")
@patch("apollo.utils.run_command.Halo")
def test_run_command_failure(mock_halo, mock_run):
    """
    Test run_command for command failure (CalledProcessError).
    """
    # Mock the spinner
    mock_spinner = MagicMock()
    mock_halo.return_value = mock_spinner

    # Mock subprocess.run to raise a CalledProcessError
    mock_error = subprocess.CalledProcessError(
        returncode=1,
        cmd="failing command",
        output="Command failed output",
        stderr="Command failed error"
    )
    mock_run.side_effect = mock_error

    # Call the function and assert it exits with an error
    command = "invalid-command"
    with pytest.raises(SystemExit):  # Exit is expected due to `exit(1)`
        run_command(command)

    # Assertions
    mock_spinner.start.assert_called_once_with("Process")
    mock_spinner.fail.assert_any_call("Process - Failed with error: ")
    mock_spinner.fail.assert_any_call("Command failed output\nCommand failed error")
    mock_run.assert_called_once_with(
        command, shell=True, cwd=None, check=True, text=True, capture_output=True
    )


@patch("apollo.utils.run_command.subprocess.run")
@patch("apollo.utils.run_command.Halo")
def test_run_command_with_cwd(mock_halo, mock_run):
    """
    Test run_command with a custom working directory.
    """
    # Mock the spinner
    mock_spinner = MagicMock()
    mock_halo.return_value = mock_spinner

    # Mock subprocess.run for a successful execution
    mock_result = MagicMock()
    mock_result.stdout = "Command executed in custom directory."
    mock_result.returncode = 0
    mock_run.return_value = mock_result

    # Call the function with a custom directory
    command = "ls"
    cwd = "/mock/directory"
    output = run_command(command, cwd=cwd)

    # Assertions
    mock_spinner.start.assert_called_once_with("Process")
    mock_spinner.succeed.assert_called_once_with("Process - Completed successfully.")
    mock_run.assert_called_once_with(
        command, shell=True, cwd=cwd, check=True, text=True, capture_output=True
    )
    assert output == "Command executed in custom directory."
    
 
 # ----------------------------------------------------------- CONFIG -----------------------------------------------------------------
    
@patch("apollo.utils.config.questionary")
def test_ensure_pypirc_creates_new_file(mock_questionary, mock_pypirc_file, monkeypatch):
    """
    Test that `ensure_pypirc` creates a new .pypirc file when none exists.
    """
    monkeypatch.setattr("os.path.expanduser", lambda path: str(mock_pypirc_file))
    
    mock_questionary.confirm.return_value.ask.return_value = True  # User agrees to create the file
    mock_questionary.text.return_value.ask.side_effect = ["__token__"]  # Mock username
    mock_questionary.password.return_value.ask.side_effect = ["test_token"]  # Mock password

    ensure_pypirc(test=True)

    # Validate the .pypirc file was created with correct content
    assert mock_pypirc_file.exists()
    config = configparser.ConfigParser()
    config.read(mock_pypirc_file)

    assert "distutils" in config.sections()
    assert "testpypi" in config.sections()
    assert config["testpypi"]["username"] == "__token__"
    assert config["testpypi"]["password"] == "test_token"


@patch("apollo.utils.config.questionary")
def test_ensure_pypirc_updates_invalid_file(mock_questionary, mock_pypirc_file, monkeypatch):
    """
    Test that `ensure_pypirc` updates an invalid .pypirc file.
    """
    # Create an invalid .pypirc file
    invalid_content = """
[distutils]
index-servers =
    testpypi

[testpypi]
repository = https://test.pypi.org/legacy/
username =
password =
"""
    mock_pypirc_file.write_text(invalid_content)
    monkeypatch.setattr("os.path.expanduser", lambda path: str(mock_pypirc_file))
    
    mock_questionary.confirm.return_value.ask.return_value = True  # User agrees to update the file
    mock_questionary.text.return_value.ask.side_effect = ["__token__"]  # Mock username
    mock_questionary.password.return_value.ask.side_effect = ["test_token"]  # Mock password

    ensure_pypirc(test=True)

    # Validate the .pypirc file was updated with correct content
    config = configparser.ConfigParser()
    config.read(mock_pypirc_file)

    assert "testpypi" in config.sections()
    assert config["testpypi"]["username"] == "__token__"
    assert config["testpypi"]["password"] == "test_token"


@patch("apollo.utils.config.questionary")
def test_ensure_pypirc_aborts_if_user_declines_creation(mock_questionary, mock_pypirc_file, monkeypatch):
    """
    Test that `ensure_pypirc` aborts if the user declines to create the file.
    """
    monkeypatch.setattr("os.path.expanduser", lambda path: str(mock_pypirc_file))
    mock_questionary.confirm.return_value.ask.return_value = False  # User declines to create the file

    with pytest.raises(SystemExit):
        ensure_pypirc(test=True)


@patch("apollo.utils.config.questionary")
def test_ensure_pypirc_valid_file_no_changes(mock_questionary, mock_pypirc_file, monkeypatch):
    """
    Test that `ensure_pypirc` does not prompt for changes if the file is already valid.
    """
    valid_content = """
[distutils]
index-servers =
    testpypi

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = test_token
"""
    mock_pypirc_file.write_text(valid_content)
    monkeypatch.setattr("os.path.expanduser", lambda path: str(mock_pypirc_file))

    ensure_pypirc(test=True)

    # Ensure questionary was not called for updates
    mock_questionary.text.assert_not_called()
    mock_questionary.password.assert_not_called()
    mock_questionary.confirm.assert_not_called()