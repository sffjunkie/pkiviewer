from pkiviewer.model import X509ExtensionTypeInfo
from pkiviewer.types import CertificateSerialNumber
from cryptography.x509.general_name import GeneralName
from cryptography.x509.extensions import AuthorityKeyIdentifier

# RFC5280 4.2.1.1
class AuthorityKeyIdentifierInfo(X509ExtensionTypeInfo):
    cert_issuer: list[GeneralName] | None
    cert_serial_number: CertificateSerialNumber | None
    key_identifier: bytes | None


def authority_key_identifier_parse(
    extension: AuthorityKeyIdentifier,
) -> AuthorityKeyIdentifierInfo:
    ext_info: AuthorityKeyIdentifierInfo = {
        "type": "AuthorityKeyIdentifier",
        "key_identifier": extension.key_identifier,
        "cert_issuer": extension.authority_cert_issuer,
        "cert_serial_number": extension.authority_cert_serial_number,
    }
    return ext_info
