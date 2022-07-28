from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

from pkiviewer.model import PublicKeyInfo


class Ed25519PublicKeyInfo(PublicKeyInfo):
    pub: bytes


def ed25519_public_key_info(key: Ed25519PublicKey) -> Ed25519PublicKeyInfo:
    public_key_info: Ed25519PublicKeyInfo = {
        "type": "ED25519",
        "name": "Edwards-curve DSA (SHA-2 & Curve25519)",
        "pub": key.public_bytes(Encoding.Raw, PublicFormat.Raw),
    }
    return public_key_info
