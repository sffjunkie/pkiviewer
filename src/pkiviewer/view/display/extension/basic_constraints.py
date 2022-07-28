from typing import cast

from pkiviewer.model.extension.basic_constraints import (
    BasicConstraintsInfo,
)
from pkiviewer.model import X509ExtensionInfo
from pkiviewer.view.console import print_value_oneline
from pkiviewer.view.theme import get_value_style
from pkiviewer.view.visibility import Visibility
from pkiviewer.context import _console  # type: ignore


# RFC5280 4.2.1.9
def basic_constraints_display(
    extension_info: X509ExtensionInfo,
    indent: int = 0,
    visibility: Visibility = Visibility.NORMAL,
) -> None:
    info = cast(BasicConstraintsInfo, extension_info["info"])
    value_style = get_value_style(visibility)
    if info["ca"]:
        text = "cA:TRUE"
    else:
        text = "cA:FALSE"
    print_value_oneline(text, indent=indent, value_style=value_style)
