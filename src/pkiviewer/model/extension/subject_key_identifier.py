from typing import cast

from cryptography.x509.extensions import ExtensionType, SubjectKeyIdentifier

from pkiviewer.types import X509ExtensionTypeInfo


# RFC5280 4.2.1.2
class SubjectKeyIdentifierInfo(X509ExtensionTypeInfo):
    key_identifier: bytes
    digest: bytes


def subject_key_identifier_parse(
    extension: ExtensionType,
) -> SubjectKeyIdentifierInfo:
    extension = cast(SubjectKeyIdentifier, extension)
    ext_info: SubjectKeyIdentifierInfo = {
        "type": "SubjectKeyIdentifier",
        "key_identifier": extension.key_identifier,
        "digest": extension.digest,
    }
    return ext_info
