from typing import cast

from cryptography.x509.extensions import ExtendedKeyUsage, ExtensionType

from pkiviewer.model import X509ExtensionTypeInfo
from pkiviewer.oid import OidNames


# RFC5280 4.2.1.12
class ExtendedKeyUsageInfo(X509ExtensionTypeInfo):
    usage: list[str]


def extended_key_usage_parse(extension: ExtensionType) -> ExtendedKeyUsageInfo:
    ext = cast(ExtendedKeyUsage, extension)

    items: list[str] = []
    for u in ext._usages:  # type: ignore
        items.append(OidNames[u.dotted_string].name)

    ext_info: ExtendedKeyUsageInfo = {"type": "ExtendedKeyUsage", "usage": items}
    return ext_info
