from cryptography.hazmat.primitives.asymmetric.dh import DHPublicKey

from pkiviewer.model import PublicKeyInfo


class DHPublicKeyInfo(PublicKeyInfo):
    key_size: int
    y: int


def dh_public_key_info(
    key: DHPublicKey,
) -> DHPublicKeyInfo:
    public_numbers = key.public_numbers()
    public_key_info: DHPublicKeyInfo = {
        "type": "DH",
        "name": "Diffie Hellman",
        "key_size": key.key_size,
        "y": public_numbers.y,
    }
    return public_key_info
