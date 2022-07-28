from typing import cast

from pkiviewer.model.extension.subject_alternative_name import (
    SubjectAlternativeNameInfo,
)
from pkiviewer.model import X509ExtensionInfo
from pkiviewer.view.console import print_value_multiline
from pkiviewer.view.theme import get_value_style
from pkiviewer.view.visibility import Visibility
from pkiviewer.context import _console  # type: ignore


# RFC5280 4.2.1.6
def subject_alternative_name_display(
    extension_info: X509ExtensionInfo,
    indent: int = 0,
    visibility: Visibility = Visibility.NORMAL,
) -> None:
    info = cast(SubjectAlternativeNameInfo, extension_info["info"])
    value_style = get_value_style(visibility)
    for name, addresses in info["sans"].items():
        items = [f"{name}:{address}" for address in addresses]
        text = ", ".join(items)
        print_value_multiline(text, indent=indent, value_style=value_style)
