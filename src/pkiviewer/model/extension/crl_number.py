from typing import cast

from cryptography.x509.extensions import CRLNumber, ExtensionType

from pkiviewer.model import X509ExtensionTypeInfo


# RFC5280 4.2.1.14
class CRLNumberInfo(X509ExtensionTypeInfo):
    crl_number: int


def crl_number_parse(
    extension: ExtensionType,
) -> CRLNumberInfo:
    ext = cast(CRLNumber, extension)
    ext_info: CRLNumberInfo = {
        "type": "CRLNumber",
        "crl_number": ext.crl_number,
    }
    return ext_info
