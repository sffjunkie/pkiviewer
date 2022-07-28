from contextvars import ContextVar

import rich.console
import rich.theme

from pkiviewer.types import Configuration

_console: ContextVar[rich.console.Console] = ContextVar("console")
_theme: ContextVar[rich.theme.Theme] = ContextVar("theme")
_config: ContextVar[Configuration] = ContextVar("config")
