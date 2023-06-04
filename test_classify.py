import pytest
from click.testing import CliRunner
from classify import main


@pytest.mark.parametrize(
    "text_input, expected_label",
    [
        ("What an idiotic statement!", "toxic"),
        ("What an idiotic statement!", "insult"),
        ("What an idiotic statement!", "obscene"),
        ("As fat as a giant hippo!", "toxic"),
        ("As fat as a giant hippo!", "insult"),
        ("Oh my goodness!", "No toxicity detected"),
        ("He is super slim", "No toxicity detected"),
    ],
)
def test_main(text_input, expected_label):
    """Function to test the toxicity classifier CLI tool with default threshold using click CliRunner"""

    runner = CliRunner()
    result = runner.invoke(main, ["--text", text_input])
    assert result.exit_code == 0
    assert expected_label in result.output


@pytest.mark.parametrize(
    "text_input, threshold_input, expected_label",
    [
        ("What an idiotic statement!", 0.9, "obscene"),
        ("As fat as a giant hippo!", 0.8, "insult"),
    ],
)
def test_threshold(text_input, threshold_input, expected_label):
    """Function to test the toxicity classifier CLI tool with custom threshold using click CliRunner"""

    runner = CliRunner()
    result = runner.invoke(main, ["--text", text_input, "--threshold", threshold_input])
    assert result.exit_code == 0
    assert expected_label not in result.output
