from typing import cast

from pkiviewer.model import X509ExtensionTypeInfo
from pkiviewer.types import CertificateSerialNumber
from cryptography.x509.general_name import GeneralName
from cryptography.x509.extensions import AuthorityKeyIdentifier, ExtensionType

# RFC5280 4.2.1.1
class AuthorityKeyIdentifierInfo(X509ExtensionTypeInfo):
    cert_issuer: list[GeneralName] | None
    cert_serial_number: CertificateSerialNumber | None
    key_identifier: bytes | None


def authority_key_identifier_parse(
    extension: ExtensionType,
) -> AuthorityKeyIdentifierInfo:
    ext = cast(AuthorityKeyIdentifier, extension)
    ext_info: AuthorityKeyIdentifierInfo = {
        "type": "AuthorityKeyIdentifier",
        "key_identifier": ext.key_identifier,
        "cert_issuer": ext.authority_cert_issuer,
        "cert_serial_number": ext.authority_cert_serial_number,
    }
    return ext_info
