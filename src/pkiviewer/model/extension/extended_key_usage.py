from typing import cast

from cryptography.x509.extensions import ExtendedKeyUsage, ExtensionType

from pkiviewer.oid.names import OidNames
from pkiviewer.types import X509ExtensionTypeInfo


# RFC5280 4.2.1.12
class ExtendedKeyUsageInfo(X509ExtensionTypeInfo):
    usage: list[str]


def extended_key_usage_parse(extension: ExtensionType) -> ExtendedKeyUsageInfo:
    extension = cast(ExtendedKeyUsage, extension)
    items: list[str] = []
    for u in extension._usages:  # type: ignore
        items.append(OidNames[u.dotted_string].name)

    ext_info: ExtendedKeyUsageInfo = {"type": "ExtendedKeyUsage", "usage": items}
    return ext_info
