import datetime
from typing import cast

from cryptography.x509 import Version

from pkiviewer.context import _console  # type: ignore
from pkiviewer.model.certificate import CertificateInfo
from pkiviewer.model.public_key.dh import DHPublicKeyInfo
from pkiviewer.model.public_key.dsa import DSAPublicKeyInfo
from pkiviewer.model.public_key.ed448 import Ed448PublicKeyInfo
from pkiviewer.model.public_key.ed25519 import Ed25519PublicKeyInfo
from pkiviewer.model.public_key.elliptic_curve import EllipticCurvePublicKeyInfo
from pkiviewer.model.public_key.rsa import RSAPublicKeyInfo
from pkiviewer.oid.names import OidNames
from pkiviewer.types import ExtensionDisplayMethod, Warning, X509ExtensionInfo
from pkiviewer.view.console import (
    print_hex_multiline,
    print_key_oneline,
    print_key_value_multiline,
    print_key_value_oneline,
)
from pkiviewer.view.display import extension
from pkiviewer.view.display.extension.header import extension_header_display
from pkiviewer.view.display.public_key import (
    dh,
    dsa,
    ed448,
    ed25519,
    elliptic_curve,
    rsa,
)
from pkiviewer.view.formatter import (
    bytes_to_hex_long,
    format_date_time,
    format_name,
    format_version,
    int_to_hex_long,
    int_to_hex_short,
)
from pkiviewer.view.theme import (
    INDENT_PER_LEVEL,
    Visibility,
    get_key_style,
    get_key_value_styles,
    get_style,
    get_value_style,
)
from pkiviewer.view.visibility import (
    get_element_visibility,
    get_extension_value_visibility,
    get_extension_visibility,
)


def serial_number_display(cert_info: CertificateInfo, indent: int = 0) -> None:
    visibility = get_element_visibility(".Data.SerialNumber")
    if visibility != Visibility.HIDDEN:
        key_style, value_style = get_key_value_styles(visibility)
        serial_number = cert_info.get("serial_number", None)
        if serial_number is not None:
            if serial_number < 2**32:
                print_key_value_oneline(
                    "Serial Number:",
                    int_to_hex_short(serial_number),
                    indent=indent,
                    key_style=key_style,
                    value_style=value_style,
                )
            else:
                print_key_value_multiline(
                    "Serial Number:",
                    int_to_hex_long(serial_number),
                    indent=indent,
                    key_style=key_style,
                    value_style=value_style,
                )


def validity_display(cert_info: CertificateInfo, indent: int = 0) -> None:
    visibility = get_element_visibility(".Data.Validity")
    if visibility != Visibility.HIDDEN:
        key_style, value_style = get_key_value_styles(visibility)
        print_key_oneline(
            "Validity:",
            indent=indent,
            key_style=key_style,
        )
        before_visibility = get_element_visibility(".Data.Validity.Before")
        if before_visibility != Visibility.HIDDEN:
            if visibility != Visibility.LOWLIGHT:
                key_style, value_style = get_key_value_styles(before_visibility)
            vbdt = cert_info.get("not_valid_before", None)
            if vbdt:
                if datetime.datetime.now() < vbdt:
                    key_style = value_style = get_style("warning")
                print_key_value_oneline(
                    "Not Before:",
                    format_date_time(vbdt),
                    indent=indent + 1,
                    key_style=key_style,
                    value_style=value_style,
                )
        after_visibility = get_element_visibility(".Data.Validity.After")
        if after_visibility != Visibility.HIDDEN:
            if visibility != Visibility.LOWLIGHT:
                key_style, value_style = get_key_value_styles(after_visibility)
            vadt = cert_info.get("not_valid_after", None)
            if vadt:
                if datetime.datetime.now() > vadt:
                    key_style = value_style = get_style("warning")
                print_key_value_oneline(
                    "Not After: ",
                    format_date_time(vadt),
                    indent=indent + 1,
                    key_style=key_style,
                    value_style=value_style,
                )


def subject_display(cert_info: CertificateInfo, indent: int = 0) -> None:
    visibility = get_element_visibility(".Data.Subject")
    if visibility != Visibility.HIDDEN:
        key_style, value_style = get_key_value_styles(visibility)

        console = _console.get()
        width = console.width
        s = cert_info.get("subject", None)
        if s is not None:
            subject = format_name(s)
            space_left = width - (indent * INDENT_PER_LEVEL) - len("Subject: ")
            if len(subject) > space_left:
                print_key_value_multiline(
                    "Subject:",
                    subject,
                    indent=indent,
                    key_style=key_style,
                    value_style=value_style,
                )
            else:
                print_key_value_oneline(
                    "Subject:",
                    subject,
                    indent=indent,
                    key_style=key_style,
                    value_style=value_style,
                )


def issuer_display(cert_info: CertificateInfo, indent: int = 0) -> None:
    visibility = get_element_visibility(".Data.Issuer")
    if visibility != Visibility.HIDDEN:
        key_style, value_style = get_key_value_styles(visibility)

        console = _console.get()
        width = console.width
        i = cert_info.get("issuer", None)
        if i is not None:
            issuer = format_name(i)
            space_left = width - (indent * INDENT_PER_LEVEL) - len("Issuer: ")
            if len(issuer) > space_left:
                print_key_value_multiline(
                    "Issuer:",
                    issuer,
                    indent=indent,
                    key_style=key_style,
                    value_style=value_style,
                )
            else:
                print_key_value_oneline(
                    "Issuer:",
                    issuer,
                    indent=indent,
                    key_style=key_style,
                    value_style=value_style,
                )


def extension_info_display(
    func: ExtensionDisplayMethod, extension_info: X509ExtensionInfo, indent: int = 0
):
    extension_type = extension_info["info"]["type"]
    visibility = get_extension_visibility(extension_type)
    if visibility != Visibility.HIDDEN:
        extension_header_display(extension_info, indent=indent + 1)

        visibility = get_extension_value_visibility(extension_type)
        if visibility != Visibility.HIDDEN:
            func(extension_info, indent + 2, visibility)


def extensions_display(cert_info: CertificateInfo, indent: int = 0) -> None:
    visibility = get_element_visibility(".Data.Extensions")
    v = cert_info.get("version", None)
    exts = cert_info.get("extensions", None)
    if v is not None and exts is not None:
        if v == Version.v3 and visibility != Visibility.HIDDEN:
            print_key_oneline("X509v3 Extensions:", indent=indent)
            for oid, extension_info in exts.items():
                try:
                    func = extension.v3_extension_display[oid]
                except KeyError:
                    func = None

                if func:
                    extension_info_display(func, extension_info, indent)
                else:
                    print(extension_info)


def fingerprint_display(cert_info: CertificateInfo, indent: int = 0) -> None:
    visibility = get_element_visibility(".Data.Fingerprint")
    if visibility != Visibility.HIDDEN:
        key_style, value_style = get_key_value_styles(visibility)
        print_key_oneline(
            "Fingerprint (SHA256):", indent=indent + 2, key_style=key_style
        )
        f = cert_info.get("fingerprint", None)
        if f is not None:
            print_hex_multiline(
                bytes_to_hex_long(f),
                stride=24,
                indent=indent + 3,
                value_style=value_style,
            )


def certificate_signature_display(cert_info: CertificateInfo, indent: int = 0) -> None:
    signature_visibility = get_element_visibility(".Signature")
    signature_algorithm_visibility = get_element_visibility(".Signature.Algorithm")
    signature_value_visibility = get_element_visibility(".Signature.Value")
    key_style = None
    value_style = None
    both_hidden = (
        signature_algorithm_visibility == Visibility.HIDDEN
        and signature_value_visibility == Visibility.HIDDEN
    )

    if signature_visibility != Visibility.HIDDEN and not both_hidden:
        key_style = get_key_style(signature_visibility)
        value_style = get_value_style(signature_visibility)

        if signature_algorithm_visibility != Visibility.HIDDEN:
            if value_style is None or signature_visibility == Visibility.NORMAL:
                value_style = get_value_style(signature_algorithm_visibility)
            sao = cert_info.get("signature_algorithm_oid", None)
            if sao:
                print_key_value_oneline(
                    "Signature:",
                    OidNames[sao].name,
                    indent=indent,
                    key_style=key_style,
                    value_style=value_style,
                )
        else:
            print_key_oneline("Signature:", indent=indent + 1)

        if signature_value_visibility != Visibility.HIDDEN:
            if value_style is None or signature_visibility == Visibility.NORMAL:
                value_style = get_value_style(signature_value_visibility)
            sig = cert_info.get("signature", None)
            if sig is not None:
                print_hex_multiline(
                    bytes_to_hex_long(sig),
                    indent=indent + 1,
                    value_style=value_style,
                )


def certificate_data_display(cert_info: CertificateInfo, indent: int = 0):
    print_key_oneline("Data:", indent=indent)

    visibility = get_element_visibility(".Data.Version")
    if visibility != Visibility.HIDDEN:
        key_style, value_style = get_key_value_styles(visibility)
        v = cert_info.get("version", None)
        if v:
            print_key_value_oneline(
                "Version:",
                format_version(v),
                indent=indent + 1,
                key_style=key_style,
                value_style=value_style,
            )

    serial_number_display(cert_info, indent=indent + 1)

    visibility = get_element_visibility(".Signature.Algorithm")
    if visibility != Visibility.HIDDEN:
        key_style, value_style = get_key_value_styles(visibility)
        sao = cert_info.get("signature_algorithm_oid", None)
        if sao is not None:
            print_key_value_oneline(
                "Signature Algorithm:",
                OidNames[sao].name,
                indent=indent + 1,
                key_style=key_style,
                value_style=value_style,
            )

    issuer_display(cert_info, indent=indent + 1)
    validity_display(cert_info, indent=indent + 1)
    subject_display(cert_info, indent=indent + 1)

    public_key = cert_info.get("public_key", None)
    if public_key is not None:
        visibility = get_element_visibility(".Data.Subject.PublicKey")
        if visibility != Visibility.HIDDEN:
            key_style, value_style = get_key_value_styles(visibility)
            print_key_oneline(
                "Subject Public Key Info:",
                indent=indent + 1,
                key_style=key_style,
            )

            if public_key["type"] == "RSA":
                rsa_key = cast(RSAPublicKeyInfo, public_key)
                rsa.print_rsa_info(rsa_key, indent=indent + 2)
            elif public_key["type"] == "EllipticCurve":
                ec_key = cast(EllipticCurvePublicKeyInfo, public_key)
                elliptic_curve.print_ec_info(ec_key, indent=indent + 2)
            elif public_key["type"] == "ED25519":
                ed25519_key = cast(Ed25519PublicKeyInfo, public_key)
                ed25519.print_ed25519_info(ed25519_key, indent=indent + 2)
            elif public_key["type"] == "ED448":
                ed448_key = cast(Ed448PublicKeyInfo, public_key)
                ed448.print_ed448_info(ed448_key, indent=indent + 2)
            elif public_key["type"] == "DH":
                dh_key = cast(DHPublicKeyInfo, public_key)
                dh.print_dh_info(dh_key, indent=indent + 2)
            elif public_key["type"] == "DSA":
                dsa_key = cast(DSAPublicKeyInfo, public_key)
                dsa.print_dsa_info(dsa_key, indent=indent + 2)
            else:
                cert_info["warnings"].append(  # type: ignore
                    Warning(
                        module="pkiviewer",
                        text=f"Unknown public key type {public_key['type']}",
                    )
                )

    fingerprint_display(cert_info, indent=indent + 1)
    extensions_display(cert_info, indent=indent + 1)


def certificate_header_display(
    cert_info: CertificateInfo, indent: int = 0, show_filename: bool = True
):
    if not show_filename:
        filename_visibility = Visibility.HIDDEN
    else:
        filename_visibility = get_element_visibility(".Header.Filename")
    filename = cert_info.get("filename", None)
    if filename_visibility == Visibility.HIDDEN or filename is None:
        print_key_oneline("Certificate:", indent=indent)
    else:
        value_style = get_style("info")
        print_key_value_oneline(
            "Certificate:", filename, indent=indent, value_style=value_style
        )


def certificate_display(
    cert_info: CertificateInfo, indent: int = 0, show_filename: bool = True
) -> None:
    visibility = get_element_visibility(".Header")
    if visibility != Visibility.HIDDEN:
        certificate_header_display(cert_info, indent, show_filename)
        indent = indent + 1

    visibility = get_element_visibility(".Data")
    if visibility != Visibility.HIDDEN:
        certificate_data_display(cert_info, indent)

    visibility = get_element_visibility(".Signature")
    if visibility != Visibility.HIDDEN:
        certificate_signature_display(cert_info, indent=indent)
