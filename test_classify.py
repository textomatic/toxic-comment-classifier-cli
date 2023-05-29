import pytest
from click.testing import CliRunner
from classify import classify_text


def test_cli():
    runner = CliRunner()
    result = runner.invoke(classify_text, ["--text", "What an idiotic statement!"])
    assert result.exit_code == 0
    assert "toxic" in result.output
    assert "insult" in result.output