import os
from unittest.mock import patch
from click.testing import CliRunner
from apollo.main import apollo


def mock_env():
    """Mock environment variables for testing."""
    with patch.dict(os.environ, {"ENV": "dev", "APOLLO_DEV_MODE": "1"}):
        yield


def test_apollo_help():
    """Test the `apollo --help` command."""
    runner = CliRunner()
    result = runner.invoke(apollo, ["--help"])
    assert result.exit_code == 0
    assert "Apollo CLI" in result.output
