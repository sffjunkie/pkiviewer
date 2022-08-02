from typing import cast

from cryptography.x509.extensions import ExtensionType, KeyUsage

from pkiviewer.types import X509ExtensionTypeInfo


# RFC5280 4.2.1.3
class KeyUsageInfo(X509ExtensionTypeInfo):
    usage: list[str]


def key_usage_parse(extension: ExtensionType) -> KeyUsageInfo:
    extension = cast(KeyUsage, extension)
    items: list[str] = []
    if extension.digital_signature:
        items.append("Digital Signature")
    if extension.content_commitment:
        items.append("Content Commitment (Non Repudiation)")
    if extension.key_encipherment:
        items.append("Key Encipherment")
    if extension.data_encipherment:
        items.append("Data Encipherment")
    if extension.key_agreement:
        items.append("Key Agreement")
    if extension.key_cert_sign:
        items.append("Certificate Sign")
    if extension.crl_sign:
        items.append("CRL Sign")
    if extension.key_agreement and extension.encipher_only:
        items.append("Encipher Only")
    if extension.key_agreement and extension.decipher_only:
        items.append("Decipher Only")

    usage: KeyUsageInfo = {"type": "KeyUsage", "usage": items}
    return usage
