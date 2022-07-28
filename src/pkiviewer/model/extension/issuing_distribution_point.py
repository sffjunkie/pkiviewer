from typing import cast

from cryptography.x509.extensions import IssuingDistributionPoint, ExtensionType

from pkiviewer.model import X509ExtensionTypeInfo, general_names_parse
from pkiviewer.model.extension.reasons import reasons_parse


# RFC5280 4.2.1.14
class IssuingDistributionPointInfo(X509ExtensionTypeInfo):
    full_name: list[tuple[str, str]]
    reasons: list[str]
    only_contains_attribute_certs: bool
    only_contains_ca_certs: bool
    only_contains_user_certs: bool
    indirect_crl: bool


def issuing_distribution_point_parse(
    extension: ExtensionType,
) -> IssuingDistributionPointInfo:
    ext = cast(IssuingDistributionPoint, extension)

    full_name = general_names_parse(ext.full_name)
    reasons = reasons_parse(ext.only_some_reasons)

    ext_info: IssuingDistributionPointInfo = {
        "type": "IssuingDistributionPoint",
        "full_name": full_name,
        "only_contains_attribute_certs": ext.only_contains_attribute_certs,
        "only_contains_ca_certs": ext.only_contains_ca_certs,
        "only_contains_user_certs": ext.only_contains_user_certs,
        "reasons": reasons,
        "indirect_crl": ext.indirect_crl,
    }
    return ext_info
