from cryptography.x509.extensions import DeltaCRLIndicator

from pkiviewer.model import X509ExtensionTypeInfo


# RFC5280 4.2.1.14
class DeltaCRLIndicatorInfo(X509ExtensionTypeInfo):
    crl_number: int


def delta_crl_indicator_parse(
    extension: DeltaCRLIndicator,
) -> DeltaCRLIndicatorInfo:
    ext_info: DeltaCRLIndicatorInfo = {
        "type": "DeltaCRLIndicator",
        "crl_number": extension.crl_number,
    }
    return ext_info
