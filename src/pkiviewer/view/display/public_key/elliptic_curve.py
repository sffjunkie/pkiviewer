from pkiviewer.model.public_key.elliptic_curve import EllipticCurvePublicKeyInfo
from pkiviewer.view.visibility import get_element_visibility, Visibility
from pkiviewer.view.console import (
    print_key_oneline,
    print_hex_multiline,
    print_key_value_oneline,
)
from pkiviewer.view.formatter import bytes_to_hex_long
from pkiviewer.view.theme import get_key_value_styles


def print_ec_info(key_info: EllipticCurvePublicKeyInfo, indent: int = 0):
    visibility = get_element_visibility(".Data.Subject.PublicKey.Algorithm")
    if visibility != Visibility.HIDDEN:
        key_style, value_style = get_key_value_styles(visibility)
        print_key_value_oneline(
            "Public Key Algorithm:",
            key_info["name"],
            indent=indent,
            key_style=key_style,
            value_style=value_style,
        )
        print_key_value_oneline(
            "Public-Key", f"({key_info['key_size']} bit)", indent=indent + 1
        )
        print_key_oneline("pub:", indent=indent + 1)
        hex_str = bytes_to_hex_long(key_info["pub"])
        print_hex_multiline(hex_str, indent=indent + 2)

        print_key_value_oneline("ASN1 OID:", key_info["asn1_oid"], indent=indent + 1)
        print_key_value_oneline(
            "NIST CURVE:", key_info["nist_curve"], indent=indent + 1
        )
