from typing import cast

from pkiviewer.model.extension.crl_number import CRLNumberInfo
from pkiviewer.types import X509ExtensionInfo
from pkiviewer.view.console import print_key_value_oneline
from pkiviewer.view.theme import get_key_style, get_value_style
from pkiviewer.view.visibility import Visibility


# RFC5280 5.2.3
def crl_number_display(
    extension_info: X509ExtensionInfo,
    indent: int = 0,
    visibility: Visibility = Visibility.NORMAL,
) -> None:
    info = cast(CRLNumberInfo, extension_info["info"])
    key_style = get_key_style(visibility)
    value_style = get_value_style(visibility)
    print_key_value_oneline(
        "CRL Number",
        info["crl_number"],
        indent=indent,
        key_style=key_style,
        value_style=value_style,
    )
