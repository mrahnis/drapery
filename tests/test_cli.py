from click.testing import CliRunner

import drapery
from drapery.cli.drape import cli

def test_drape():
    runner = CliRunner()
    result = runner.invoke(cli, ['--help'])
    assert result.exit_code == 0
