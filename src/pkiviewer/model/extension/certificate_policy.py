from typing import cast, TypedDict

from cryptography.x509 import UserNotice
from cryptography.x509.extensions import CertificatePolicies, ExtensionType

from pkiviewer.model import X509ExtensionTypeInfo
from pkiviewer.oid import Oid


# RFC5280 4.2.1.4
class PolicyInfo(TypedDict):
    oid: Oid
    strings: list[str]
    user_notices: list[UserNotice]


class CertificatePoliciesInfo(X509ExtensionTypeInfo):
    policies: list[PolicyInfo]


def certificate_policies_parse(extension: ExtensionType) -> CertificatePoliciesInfo:
    ext = cast(CertificatePolicies, extension)
    policies: list[PolicyInfo] = []
    for policy in ext._policies:  # type: ignore
        oid = policy.policy_identifier.dotted_string

        strings: list[str] = []
        user_notices: list[UserNotice] = []
        if policy.policy_qualifiers:
            for qual in policy.policy_qualifiers:
                if isinstance(qual, str):
                    strings.append(qual)
                else:
                    user_notices.append(qual)

        policy_info: PolicyInfo = {
            "oid": oid,
            "strings": strings,
            "user_notices": user_notices,
        }

        # if isinstance(policy, )
        policies.append(policy_info)
    ext_info: CertificatePoliciesInfo = {
        "type": "CertificatePolicies",
        "policies": policies,
    }
    return ext_info
