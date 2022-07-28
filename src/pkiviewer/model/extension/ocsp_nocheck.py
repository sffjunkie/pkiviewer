# from typing import cast

# from cryptography.x509.extensions import OCSPNoCheck
from cryptography.x509.extensions import ExtensionType

from pkiviewer.model import X509ExtensionTypeInfo


# RFC2560 4.2.2.2.1
class OCSPNoCheckInfo(X509ExtensionTypeInfo):
    nocheck: bool


def ocsp_nocheck_parse(extension: ExtensionType) -> OCSPNoCheckInfo:
    # ext = cast(OCSPNoCheck, extension)
    ext_info: OCSPNoCheckInfo = {
        "type": "OCSPNoCheck",
        "nocheck": True,
    }
    return ext_info
