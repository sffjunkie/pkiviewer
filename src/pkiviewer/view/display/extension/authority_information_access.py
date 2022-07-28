from typing import cast

from pkiviewer.model.extension.authority_information_access import (
    AuthorityInformationAccessInfo,
)
from pkiviewer.model import X509ExtensionInfo
from pkiviewer.view.console import print_value_oneline
from pkiviewer.view.theme import get_value_style
from pkiviewer.view.visibility import Visibility
from pkiviewer.context import _console  # type: ignore


# RFC5280 4.2.2.1
def authority_information_access_display(
    extension_info: X509ExtensionInfo,
    indent: int = 0,
    visibility: Visibility = Visibility.NORMAL,
) -> None:
    info = cast(AuthorityInformationAccessInfo, extension_info["info"])
    value_style = get_value_style(visibility)
    for description in info["access_descriptions"]:
        print_value_oneline(
            f"{description[0]} - {description[1]}:{description[2]}",
            indent=indent,
            value_style=value_style,
        )
