from typing import cast

from pkiviewer.model.extension.extended_key_usage import (
    ExtendedKeyUsageInfo,
)
from pkiviewer.model import X509ExtensionInfo
from pkiviewer.view.console import print_value_oneline
from pkiviewer.view.theme import get_value_style
from pkiviewer.view.visibility import Visibility


# RFC5280 4.2.1.12
def extended_key_usage_display(
    extension_info: X509ExtensionInfo,
    indent: int = 0,
    visibility: Visibility = Visibility.NORMAL,
) -> None:
    info = cast(ExtendedKeyUsageInfo, extension_info["info"])
    value_style = get_value_style(visibility)
    text = ", ".join(info["usage"])
    print_value_oneline(text, indent=indent, value_style=value_style)
