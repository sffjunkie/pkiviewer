from typing import cast

from pkiviewer.model.extension.issuing_distribution_point import (
    IssuingDistributionPointInfo,
)
from pkiviewer.types import X509ExtensionInfo
from pkiviewer.view.console import print_key_oneline, print_value_oneline
from pkiviewer.view.theme import get_key_style, get_value_style
from pkiviewer.view.visibility import Visibility


# RFC5280 5.2.5
def issuing_distribution_point_display(
    extension_info: X509ExtensionInfo,
    indent: int = 0,
    visibility: Visibility = Visibility.NORMAL,
) -> None:
    info = cast(IssuingDistributionPointInfo, extension_info["info"])
    key_style = get_key_style(visibility)
    value_style = get_value_style(visibility)
    print_key_oneline(
        "Issuing Distribution Point:",
        indent=indent,
        key_style=key_style,
    )

    print_key_oneline(
        "Full Name:",
        indent=indent + 1,
        key_style=key_style,
    )

    for item in info["full_name"]:
        print_value_oneline(
            f"{item[0]}: {item[1]}",
            indent=indent + 2,
            value_style=value_style,
        )
