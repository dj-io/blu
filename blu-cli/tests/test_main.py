import os
from unittest.mock import patch
from click.testing import CliRunner
from blu.main import blu


def mock_env():
    """Mock environment variables for testing."""
    with patch.dict(os.environ, {"ENV": "dev", "blu_DEV_MODE": "1"}):
        yield


def test_apollo_help():
    """Test the `apollo --help` command."""
    runner = CliRunner()
    result = runner.invoke(blu, ["--help"])
    assert result.exit_code == 0
    assert "BLU CLI" in result.output
