from typing import cast

from cryptography.x509.extensions import CRLDistributionPoints, ExtensionType

from pkiviewer.model import (
    X509ExtensionTypeInfo,
    general_names_parse,
    relative_distinguished_names_parse,
    GeneralNameInfo,
)
from pkiviewer.model.extension.reasons import reasons_parse
from pkiviewer.model import DistributionPointInfo


# RFC5280 4.2.1.13
class CRLDistributionPointsInfo(X509ExtensionTypeInfo):
    distribution_points: list[DistributionPointInfo]


def crl_distribution_points_parse(
    extension: ExtensionType,
) -> CRLDistributionPointsInfo:
    ext = cast(CRLDistributionPoints, extension)
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
    ext_info: CRLDistributionPointsInfo = {
        "type": "CRLDistributionPoints",
        "distribution_points": distribution_points,
    }
    return ext_info
