from typing import cast

from cryptography.x509.extensions import SubjectKeyIdentifier, ExtensionType

from pkiviewer.model import X509ExtensionTypeInfo


# RFC5280 4.2.1.2
class SubjectKeyIdentifierInfo(X509ExtensionTypeInfo):
    key_identifier: bytes
    digest: bytes


def subject_key_identifier_parse(extension: ExtensionType) -> SubjectKeyIdentifierInfo:
    ext = cast(SubjectKeyIdentifier, extension)
    ext_info: SubjectKeyIdentifierInfo = {
        "type": "SubjectKeyIdentifier",
        "key_identifier": ext.key_identifier,
        "digest": ext.digest,
    }
    return ext_info
