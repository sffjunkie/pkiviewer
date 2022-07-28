from typing import cast

from pkiviewer.model.extension.inhibit_any_policy import (
    InhibitAnyPolicyInfo,
)
from pkiviewer.model import X509ExtensionInfo
from pkiviewer.view.console import print_key_value_oneline
from pkiviewer.view.theme import get_value_style, get_key_style
from pkiviewer.view.visibility import Visibility


# RFC5280 4.2.1.14
def inhibit_any_policy_display(
    extension_info: X509ExtensionInfo,
    indent: int = 0,
    visibility: Visibility = Visibility.NORMAL,
) -> None:
    info = cast(InhibitAnyPolicyInfo, extension_info["info"])
    key_style = get_key_style(visibility)
    value_style = get_value_style(visibility)
    print_key_value_oneline(
        "Skip Certs:",
        str(info["skip_certs"]),
        indent=indent,
        key_style=key_style,
        value_style=value_style,
    )
