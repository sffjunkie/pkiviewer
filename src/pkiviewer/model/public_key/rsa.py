from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey

from pkiviewer.model import PublicKeyInfo


class RSAPublicKeyInfo(PublicKeyInfo):
    key_size: int
    modulus: int
    exponent: int


def rsa_public_key_info(key: RSAPublicKey) -> RSAPublicKeyInfo:
    public_numbers = key.public_numbers()
    public_key_info: RSAPublicKeyInfo = {
        "type": "RSA",
        "name": "Rivest, Shamir, and Adleman DSA",
        "key_size": key.key_size,
        "modulus": public_numbers.n,
        "exponent": public_numbers.e,
    }
    return public_key_info
