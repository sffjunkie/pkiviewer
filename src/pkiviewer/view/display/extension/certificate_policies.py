from typing import cast

from pkiviewer.model.extension.certificate_policy import (
    CertificatePoliciesInfo,
)
from pkiviewer.model import X509ExtensionInfo
from pkiviewer.oid import OidNames
from pkiviewer.view.console import print_value_multiline, print_key_oneline
from pkiviewer.view.theme import get_value_style, get_key_style
from pkiviewer.view.visibility import Visibility
from pkiviewer.context import _console  # type: ignore


# RFC5280 4.2.1.4
def policy_value_display(
    value: str,
    indent: int = 0,
    visibility: Visibility = Visibility.NORMAL,
) -> None:
    value_style = get_value_style(visibility)
    idx = value.find("https://")
    if idx == -1:
        idx = value.find("http://")

        if idx == -1:
            text = value
            url = ""
        else:
            text = value[:idx]
            url = value[idx:]
    else:
        text = value[:idx]
        url = value[idx:]

    text = text.strip()
    url = url.strip()

    value_style = get_value_style(visibility)
    print_value_multiline(text, indent, value_style=value_style)
    if url:
        print_value_multiline(url, indent, value_style=value_style)


def certificate_policies_display(
    extension_info: X509ExtensionInfo,
    indent: int,
    visibility: Visibility = Visibility.NORMAL,
) -> None:
    info = cast(CertificatePoliciesInfo, extension_info["info"])
    key_style = get_key_style(visibility)
    for policy in info["policies"]:
        oid = policy["oid"]
        print_key_oneline("Policy:", indent, key_style=key_style)
        policy_value_display(OidNames[oid].name, indent + 1, visibility)
