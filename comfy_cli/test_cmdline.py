from typer.testing import CliRunner

from .cmdline import app

runner = CliRunner()


def test_app():
    result = runner.invoke(
        app,
        ["--here", "--skip-prompt", "install", "--cpu"],
    )
    print("Stdout:")
    print(result.stdout)
    assert result.exit_code == 0


def test_app():
    result = runner.invoke(
        app,
        ["--here", "--skip-prompt", "install", "--cpu"],
    )
    print("Stdout:")
    print(result.stdout)
    assert result.exit_code == 0
