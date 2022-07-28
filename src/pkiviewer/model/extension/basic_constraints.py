from typing import cast

from cryptography.x509.extensions import BasicConstraints, ExtensionType

from pkiviewer.model import X509ExtensionTypeInfo


# RFC5280 4.2.1.9
class BasicConstraintsInfo(X509ExtensionTypeInfo):
    ca: bool
    path_length: int


def basic_constraints_parse(extension: ExtensionType) -> BasicConstraintsInfo:
    ext = cast(BasicConstraints, extension)
    path_length = ext.path_length if ext.path_length else 0
    ext_info: BasicConstraintsInfo = {
        "type": "BasicConstraints",
        "ca": ext.ca,
        "path_length": path_length,
    }
    return ext_info
