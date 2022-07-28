from typing import cast

from pkiviewer.model.extension.subject_key_identifier import (
    SubjectKeyIdentifierInfo,
)
from pkiviewer.model import X509ExtensionInfo
from pkiviewer.view.formatter import bytes_to_hex_long
from pkiviewer.view.console import print_value_oneline
from pkiviewer.view.theme import get_value_style
from pkiviewer.view.visibility import Visibility
from pkiviewer.context import _console  # type: ignore


# RFC5280 4.2.1.2
def subject_key_identifier_display(
    extension_info: X509ExtensionInfo,
    indent: int = 0,
    visibility: Visibility = Visibility.NORMAL,
) -> None:
    info = cast(SubjectKeyIdentifierInfo, extension_info["info"])
    value_style = get_value_style(visibility)
    text = bytes_to_hex_long(info["key_identifier"])
    print_value_oneline(text, indent=indent, value_style=value_style)
