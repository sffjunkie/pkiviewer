from typing import cast

from pkiviewer.model import X509ExtensionInfo
from pkiviewer.model.extension.authority_key_identifier import (
    AuthorityKeyIdentifierInfo,
)
from pkiviewer.view.formatter import bytes_to_hex_long
from pkiviewer.view.console import (
    print_key_oneline,
    print_hex_multiline,
    print_key_value_multiline,
)
from pkiviewer.view.theme import get_key_style, get_value_style, INDENT_PER_LEVEL
from pkiviewer.view.visibility import Visibility
from pkiviewer.context import _console  # type: ignore

# RFC5280 4.2.1.1
# TODO: authority_key_identifier_display  cert_issuer, cert_serial_number
def authority_key_identifier_display(
    extension_info: X509ExtensionInfo,
    indent: int = 0,
    visibility: Visibility = Visibility.NORMAL,
) -> None:
    info = cast(AuthorityKeyIdentifierInfo, extension_info["info"])
    key_style = get_key_style(visibility)
    value_style = get_value_style(visibility)
    text = bytes_to_hex_long(info["key_identifier"])

    c = _console.get()
    remaining_space = c.width - len("keyIdentifier:") - (indent * INDENT_PER_LEVEL)
    if len(text) > remaining_space:
        print_key_oneline("keyIdentifier:", indent, key_style=key_style)
        print_hex_multiline(text, indent=indent, value_style=value_style)
    else:
        print_key_value_multiline(
            "keyIdentifier:",
            text,
            indent=indent,
            key_style=key_style,
            value_style=value_style,
        )
