from cryptography.hazmat.primitives.asymmetric.dsa import DSAPublicKey

from pkiviewer.model import PublicKeyInfo


class DSAPublicKeyInfo(PublicKeyInfo):
    key_size: int
    y: int


def dsa_public_key_info(
    key: DSAPublicKey,
) -> DSAPublicKeyInfo:
    public_numbers = key.public_numbers()
    public_key_info: DSAPublicKeyInfo = {
        "type": "DSA",
        "name": "Digital Signature Algorithm",
        "key_size": key.key_size,
        "y": public_numbers.y,
    }
    return public_key_info
