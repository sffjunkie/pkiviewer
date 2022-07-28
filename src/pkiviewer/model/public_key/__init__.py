from cryptography.hazmat.primitives.asymmetric.dh import DHPublicKey
from cryptography.hazmat.primitives.asymmetric.dsa import DSAPublicKey
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePublicKey
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
from cryptography.hazmat.primitives.asymmetric.ed448 import Ed448PublicKey
from cryptography.hazmat.primitives.asymmetric.types import CERTIFICATE_PUBLIC_KEY_TYPES

from pkiviewer.model import PublicKeyInfo
from pkiviewer.model.public_key.dh import dh_public_key_info
from pkiviewer.model.public_key.dsa import dsa_public_key_info
from pkiviewer.model.public_key.ed448 import ed448_public_key_info
from pkiviewer.model.public_key.ed25519 import ed25519_public_key_info
from pkiviewer.model.public_key.elliptic_curve import elliptic_curve_public_key_info
from pkiviewer.model.public_key.rsa import rsa_public_key_info


def public_key_info(pk: CERTIFICATE_PUBLIC_KEY_TYPES) -> PublicKeyInfo | None:
    if isinstance(pk, RSAPublicKey):
        return rsa_public_key_info(pk)
    elif isinstance(pk, EllipticCurvePublicKey):
        return elliptic_curve_public_key_info(pk)
    elif isinstance(pk, DHPublicKey):
        return dh_public_key_info(pk)
    elif isinstance(pk, DSAPublicKey):
        return dsa_public_key_info(pk)
    elif isinstance(pk, Ed25519PublicKey):
        return ed25519_public_key_info(pk)
    elif isinstance(pk, Ed448PublicKey):
        return ed448_public_key_info(pk)
    else:
        return None
