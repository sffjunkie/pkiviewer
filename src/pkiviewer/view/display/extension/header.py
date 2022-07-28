from pkiviewer.model import X509ExtensionInfo
from pkiviewer.view.console import print_key_value_oneline
from pkiviewer.view.theme import get_key_style, get_style, get_value_style
from pkiviewer.view.visibility import (
    get_element_visibility,
    get_extension_value_visibility,
    Visibility,
)


def extension_header_display(extension_info: X509ExtensionInfo, indent: int):
    extension_name = extension_info["name"]
    extension_type = extension_info["info"]["type"]

    critical_visibility = get_element_visibility(".Data.Extension.Critical")
    if extension_info["critical"] and critical_visibility != Visibility.HIDDEN:
        critical = "critical"
    else:
        critical = ""

    value_visibility = get_extension_value_visibility(extension_type)
    if value_visibility != Visibility.HIDDEN:
        extension_name += ":"

    key_style = get_key_style(Visibility.NORMAL)
    if critical_visibility != Visibility.LOWLIGHT:
        critical_style = get_style("extension_critical")
    else:
        critical_style = get_value_style(critical_visibility)

    print_key_value_oneline(
        extension_name,
        critical,
        indent=indent,
        key_style=key_style,
        value_style=critical_style,
    )
