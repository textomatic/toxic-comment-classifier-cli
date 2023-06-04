import pytest
from click.testing import CliRunner
from classify import main


@pytest.mark.parametrize(
    "text_input, expected_labels",
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
def test_main(text_input, expected_labels):
    runner = CliRunner()
    result = runner.invoke(main, ["--text", text_input])
    assert result.exit_code == 0
    assert expected_labels in result.output
