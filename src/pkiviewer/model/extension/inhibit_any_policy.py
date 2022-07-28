from typing import cast

from cryptography.x509.extensions import InhibitAnyPolicy, ExtensionType

from pkiviewer.model import X509ExtensionTypeInfo


# RFC5280 4.2.1.14
class InhibitAnyPolicyInfo(X509ExtensionTypeInfo):
    skip_certs: int


def inhibit_any_policy_parse(
    extension: ExtensionType,
) -> InhibitAnyPolicyInfo:
    ext = cast(InhibitAnyPolicy, extension)
    ext_info: InhibitAnyPolicyInfo = {
        "type": "InhibitAnyPolicyInfo",
        "skip_certs": ext.skip_certs,
    }
    return ext_info
