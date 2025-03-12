import os
from unittest.mock import patch
from click.testing import CliRunner
from sun.main import sunday


def mock_env():
    """Mock environment variables for testing."""
    with patch.dict(os.environ, {"ENV": "dev", "SUN_DEV_MODE": "1"}):
        yield


def test_apollo_help():
    """Test the `apollo --help` command."""
    runner = CliRunner()
    result = runner.invoke(sunday, ["--help"])
    assert result.exit_code == 0
    assert "Sunday CLI" in result.output
