from typing import cast

from cryptography.x509.extensions import ExtensionType, IssuingDistributionPoint

from pkiviewer.model import general_names_parse
from pkiviewer.model.extension.reasons import reasons_parse
from pkiviewer.types import X509ExtensionTypeInfo


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
    extension = cast(IssuingDistributionPoint, extension)
    full_name = general_names_parse(extension.full_name)
    reasons = reasons_parse(extension.only_some_reasons)

    ext_info: IssuingDistributionPointInfo = {
        "type": "IssuingDistributionPoint",
        "full_name": full_name,
        "only_contains_attribute_certs": extension.only_contains_attribute_certs,
        "only_contains_ca_certs": extension.only_contains_ca_certs,
        "only_contains_user_certs": extension.only_contains_user_certs,
        "reasons": reasons,
        "indirect_crl": extension.indirect_crl,
    }
    return ext_info
