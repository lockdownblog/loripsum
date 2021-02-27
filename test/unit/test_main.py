import pytest
from unittest.mock import patch
from click.testing import CliRunner
from loripsum.__main__ import main

def test_main():
    runner = CliRunner()
    with patch("loripsum.__main__.get_text") as get_text_patched:
        result = runner.invoke(main, ['2'])
        get_text_patched.assert_called_once_with(2)
    assert result.exit_code == 0


def test_main_fails_with_string():
    runner = CliRunner()

    with patch("loripsum.__main__.get_text") as get_text_patched:
        result = runner.invoke(main, ['"hola mundo"'])
        get_text_patched.assert_not_called()

    assert result.exit_code != 0

