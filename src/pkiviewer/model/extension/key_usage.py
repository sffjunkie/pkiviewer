from typing import cast

from cryptography.x509.extensions import KeyUsage, ExtensionType

from pkiviewer.model import X509ExtensionTypeInfo


# RFC5280 4.2.1.3
class KeyUsageInfo(X509ExtensionTypeInfo):
    usage: list[str]


def key_usage_parse(extension: ExtensionType) -> KeyUsageInfo:
    items: list[str] = []
    ext = cast(KeyUsage, extension)
    if ext.digital_signature:
        items.append("Digital Signature")
    if ext.content_commitment:
        items.append("Content Commitment (Non Repudiation)")
    if ext.key_encipherment:
        items.append("Key Encipherment")
    if ext.data_encipherment:
        items.append("Data Encipherment")
    if ext.key_agreement:
        items.append("Key Agreement")
    if ext.key_cert_sign:
        items.append("Certificate Sign")
    if ext.crl_sign:
        items.append("CRL Sign")
    if ext.key_agreement and ext.encipher_only:
        items.append("Encipher Only")
    if ext.key_agreement and ext.decipher_only:
        items.append("Decipher Only")

    usage: KeyUsageInfo = {"type": "KeyUsage", "usage": items}
    return usage
