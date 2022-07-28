from typing import cast

from pkiviewer.model.extension.name_constraints import (
    NameConstraintsInfo,
)
from pkiviewer.model import X509ExtensionInfo
from pkiviewer.view.console import print_value_oneline
from pkiviewer.view.theme import get_value_style
from pkiviewer.view.visibility import Visibility


# RFC5280 4.2.1.10
def name_constraints_display(
    extension_info: X509ExtensionInfo,
    indent: int = 0,
    visibility: Visibility = Visibility.NORMAL,
) -> None:
    info = cast(NameConstraintsInfo, extension_info["info"])
    value_style = get_value_style(visibility)
    for name in info["permitted_subtrees"]:
        print_value_oneline(
            f"{name[0]}:{name[1]}", indent=indent, value_style=value_style
        )
