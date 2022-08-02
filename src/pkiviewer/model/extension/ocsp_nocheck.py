from typing import cast

from cryptography.x509.extensions import ExtensionType, OCSPNoCheck

from pkiviewer.types import X509ExtensionTypeInfo


# RFC2560 4.2.2.2.1
class OCSPNoCheckInfo(X509ExtensionTypeInfo):
    nocheck: bool


def ocsp_nocheck_parse(extension: ExtensionType) -> OCSPNoCheckInfo:
    extension = cast(OCSPNoCheck, extension)
    ext_info: OCSPNoCheckInfo = {
        "type": "OCSPNoCheck",
        "nocheck": True,
    }
    return ext_info
