from cryptography.hazmat.primitives.asymmetric.ed448 import Ed448PublicKey
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

from pkiviewer.model import PublicKeyInfo


class Ed448PublicKeyInfo(PublicKeyInfo):
    pub: bytes


def ed448_public_key_info(key: Ed448PublicKey) -> Ed448PublicKeyInfo:
    public_key_info: Ed448PublicKeyInfo = {
        "type": "ED448",
        "name": "",
        "pub": key.public_bytes(Encoding.Raw, PublicFormat.Raw),
    }
    return public_key_info
