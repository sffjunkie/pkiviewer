from pkiviewer.model.public_key.rsa import RSAPublicKeyInfo
from pkiviewer.view.visibility import get_element_visibility, Visibility
from pkiviewer.view.console import (
    print_hex_multiline,
    print_key_oneline,
    print_key_value_oneline,
)
from pkiviewer.view.formatter import int_to_hex_long
from pkiviewer.view.theme import get_key_value_styles


def print_rsa_info(key_info: RSAPublicKeyInfo, indent: int = 0):
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
            "RSA Public-Key", f"({key_info['key_size']} bit)", indent=indent + 1
        )
        print_key_oneline("Modulus:", indent=indent + 1)
        print_hex_multiline(int_to_hex_long(key_info["modulus"]), indent=indent + 2)
        print_key_value_oneline(
            "Exponent",
            f"{key_info['exponent']} ({hex(key_info['exponent'])})",
            indent=indent + 1,
        )
