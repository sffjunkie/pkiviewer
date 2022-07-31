from cryptography.x509.extensions import BasicConstraints

from pkiviewer.model import X509ExtensionTypeInfo


# RFC5280 4.2.1.9
class BasicConstraintsInfo(X509ExtensionTypeInfo):
    ca: bool
    path_length: int


def basic_constraints_parse(extension: BasicConstraints) -> BasicConstraintsInfo:
    path_length = extension.path_length if extension.path_length else 0
    ext_info: BasicConstraintsInfo = {
        "type": "BasicConstraints",
        "ca": extension.ca,
        "path_length": path_length,
    }
    return ext_info
