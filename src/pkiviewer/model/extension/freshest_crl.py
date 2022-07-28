from typing import cast

from cryptography.x509.extensions import FreshestCRL, ExtensionType

from pkiviewer.model import (
    X509ExtensionTypeInfo,
    DistributionPointInfo,
    general_names_parse,
    relative_distinguished_names_parse,
    GeneralNameInfo,
)
from pkiviewer.model.extension.reasons import reasons_parse

# RFC5280 4.2.1.14
class FreshestCRLInfo(X509ExtensionTypeInfo):
    distribution_points: list[DistributionPointInfo]


def freshest_crl_parse(
    extension: ExtensionType,
) -> FreshestCRLInfo:
    ext = cast(FreshestCRL, extension)

    distribution_points: list[DistributionPointInfo] = []
    for dp in ext._distribution_points:  # type: ignore
        names: list[GeneralNameInfo] = []

        if dp.full_name:
            names = general_names_parse(dp.full_name)
        elif dp.relative_name:
            names = relative_distinguished_names_parse(dp.relative_name)
        else:
            names = []

        dpi: DistributionPointInfo = {
            "names": names,
            "crl_issuer": general_names_parse(dp.crl_issuer),
            "reasons": reasons_parse(dp.reasons),
        }

        distribution_points.append(dpi)

    ext_info: FreshestCRLInfo = {
        "type": "FreshestCRL",
        "distribution_points": distribution_points,
    }

    return ext_info
