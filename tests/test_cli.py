from click.testing import CliRunner

import drapery
from drapery.cli import drape


def test_err(tmpdir):
    runner = CliRunner()
    result = runner.invoke(drape, ['--help'])
    assert result.exit_code == 0
