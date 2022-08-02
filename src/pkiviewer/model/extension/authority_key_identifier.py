from typing import cast

from cryptography.x509.extensions import AuthorityKeyIdentifier, ExtensionType
from cryptography.x509.general_name import GeneralName

from pkiviewer.types import CertificateSerialNumber, X509ExtensionTypeInfo


# RFC5280 4.2.1.1
class AuthorityKeyIdentifierInfo(X509ExtensionTypeInfo):
    cert_issuer: list[GeneralName] | None
    cert_serial_number: CertificateSerialNumber | None
    key_identifier: bytes | None


def authority_key_identifier_parse(
    extension: ExtensionType,
) -> AuthorityKeyIdentifierInfo:
    extension = cast(AuthorityKeyIdentifier, extension)
    ext_info: AuthorityKeyIdentifierInfo = {
        "type": "AuthorityKeyIdentifier",
        "key_identifier": extension.key_identifier,
        "cert_issuer": extension.authority_cert_issuer,
        "cert_serial_number": extension.authority_cert_serial_number,
    }
    return ext_info
