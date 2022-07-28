import rich.theme
import rich.console
from pkiviewer.context import _console, _theme, _config  # type: ignore


def rich_init(**kwargs: object):
    config = _config.get()

    theme = rich.theme.Theme(config["theme"])
    _theme.set(theme)

    console = rich.console.Console(**kwargs)
    _console.set(console)
