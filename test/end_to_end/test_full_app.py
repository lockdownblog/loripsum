from click.testing import CliRunner
from loripsum.__main__ import main


def test_main():
    runner = CliRunner()
    result = runner.invoke(main, ['3'])

    string_result = [par for par in result.output.split('\n') if par]

    assert len(string_result) == 3
    assert result.exit_code == 0