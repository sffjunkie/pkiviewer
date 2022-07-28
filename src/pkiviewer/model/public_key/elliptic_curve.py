from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePublicKey
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

from pkiviewer.model import PublicKeyInfo


class EllipticCurvePublicKeyInfo(PublicKeyInfo):
    key_size: int
    x: int
    y: int
    pub: bytes
    asn1_oid: str
    nist_curve: str


def elliptic_curve_public_key_info(
    key: EllipticCurvePublicKey,
) -> EllipticCurvePublicKeyInfo:
    public_numbers = key.public_numbers()
    public_key_info: EllipticCurvePublicKeyInfo = {
        "type": "EllipticCurve",
        "name": "Elliptic Curve",
        "key_size": key.key_size,
        "x": public_numbers.x,
        "y": public_numbers.y,
        "pub": key.public_bytes(Encoding.X962, PublicFormat.UncompressedPoint),
        "asn1_oid": public_numbers.curve.name,
        "nist_curve": f"P-{public_numbers.curve.key_size}",
    }
    return public_key_info
