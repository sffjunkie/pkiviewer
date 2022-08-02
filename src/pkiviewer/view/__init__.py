import rich.console
import rich.theme

from pkiviewer.context import _config, _console, _err_console, _theme  # type: ignore


def rich_init(**kwargs: object):
    config = _config.get()

    theme = rich.theme.Theme(config["theme"])
    _theme.set(theme)

    console = rich.console.Console(**kwargs)
    _console.set(console)

    err_console_args = kwargs.copy()
    err_console_args["stderr"] = True
    err_console = rich.console.Console(**err_console_args)
    _err_console.set(err_console)
