from typing import cast

from pkiviewer.model.extension.freshest_crl import FreshestCRLInfo
from pkiviewer.types import X509ExtensionInfo
from pkiviewer.view.console import print_key_oneline, print_value_oneline
from pkiviewer.view.theme import get_key_style, get_value_style
from pkiviewer.view.visibility import Visibility


# RFC5280 4.2.1.15
def freshest_crl_display(
    extension_info: X509ExtensionInfo,
    indent: int = 0,
    visibility: Visibility = Visibility.NORMAL,
) -> None:
    info = cast(FreshestCRLInfo, extension_info["info"])
    key_style = get_key_style(visibility)
    value_style = get_value_style(visibility)
    key_indent = indent
    value_indent = indent + 1
    for dpi in info["distribution_points"]:
        if dpi["names"]:
            print_key_oneline("Full Name:", key_indent + 1, key_style=key_style)
            for name in dpi["names"]:
                print_value_oneline(
                    f"{name[0]}:{name[1]}",
                    indent=value_indent,
                    value_style=value_style,
                )

        if dpi["crl_issuer"]:
            print_key_oneline("CRL Issuer:", key_indent + 1, key_style=key_style)
            for issuer in dpi["crl_issuer"]:
                print_value_oneline(
                    f"{issuer[0]}: {issuer[1]}",
                    indent=value_indent,
                    value_style=value_style,
                )

        if dpi["reasons"]:
            print_key_oneline("Reasons:", key_indent, key_style=key_style)
            for reason in dpi["reasons"]:
                print_value_oneline(
                    reason, indent=value_indent, value_style=value_style
                )
