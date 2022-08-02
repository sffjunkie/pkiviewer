from typing import cast

from cryptography.x509.extensions import ExtensionType, InhibitAnyPolicy

from pkiviewer.types import X509ExtensionTypeInfo


# RFC5280 4.2.1.14
class InhibitAnyPolicyInfo(X509ExtensionTypeInfo):
    skip_certs: int


def inhibit_any_policy_parse(
    extension: ExtensionType,
) -> InhibitAnyPolicyInfo:
    extension = cast(InhibitAnyPolicy, extension)
    ext_info: InhibitAnyPolicyInfo = {
        "type": "InhibitAnyPolicyInfo",
        "skip_certs": extension.skip_certs,
    }
    return ext_info
