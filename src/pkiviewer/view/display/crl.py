from pkiviewer.context import _console  # type: ignore; type: ignore
from pkiviewer.model.crl import CertificateRevocationListInfo
from pkiviewer.oid.names import OidNames
from pkiviewer.view.console import (
    print_hex_multiline,
    print_key_oneline,
    print_key_value_multiline,
    print_key_value_oneline,
)
from pkiviewer.view.display import extension
from pkiviewer.view.formatter import bytes_to_hex_long, format_date_time, format_name
from pkiviewer.view.theme import (
    INDENT_PER_LEVEL,
    Visibility,
    get_key_style,
    get_key_value_styles,
    get_value_style,
)
from pkiviewer.view.visibility import get_element_visibility


def issuer_display(crl_info: CertificateRevocationListInfo, indent: int = 0) -> None:
    visibility = get_element_visibility(".Data.Issuer")
    if visibility != Visibility.HIDDEN:
        key_style, value_style = get_key_value_styles(visibility)

        console = _console.get()
        width = console.width
        issuer = format_name(crl_info["issuer"])
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


def extensions_display(
    crl_info: CertificateRevocationListInfo, indent: int = 0
) -> None:
    visibility = get_element_visibility(".Data.Extensions")
    if visibility != Visibility.HIDDEN:
        print_key_oneline("X509v3 Extensions:", indent=indent)
        for oid, extension_info in crl_info["extensions"].items():
            try:
                func = extension.v3_extension_display[oid]
            except KeyError:
                func = None

            if func:
                func(extension_info, indent + 1, visibility)
            else:
                print(extension_info)


def fingerprint_display(
    crl_info: CertificateRevocationListInfo, indent: int = 0
) -> None:
    visibility = get_element_visibility(".Data.Fingerprint")
    if visibility != Visibility.HIDDEN:
        key_style, value_style = get_key_value_styles(visibility)
        print_key_oneline("Fingerprint (SHA256):", indent=2, key_style=key_style)
        print_hex_multiline(
            bytes_to_hex_long(crl_info["fingerprint"]),
            stride=16,
            indent=3,
            value_style=value_style,
        )


def signature_display(crl_info: CertificateRevocationListInfo, indent: int = 0) -> None:
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
            # if key_style is None or signature_visibility == Visibility.NORMAL:
            #     key_style = get_key_style(signature_algorithm_visibility)
            if value_style is None or signature_visibility == Visibility.NORMAL:
                value_style = get_value_style(signature_algorithm_visibility)
            print_key_value_oneline(
                "Signature:",
                OidNames[crl_info["signature_algorithm_oid"]].name,
                indent=indent,
                key_style=key_style,
                value_style=value_style,
            )
        else:
            print_key_oneline("Signature:", indent=1)

        if signature_value_visibility != Visibility.HIDDEN:
            if value_style is None or signature_visibility == Visibility.NORMAL:
                value_style = get_value_style(signature_value_visibility)
            print_hex_multiline(
                bytes_to_hex_long(crl_info["signature"]),
                indent=indent + 1,
                value_style=value_style,
            )


def crl_display(crl_info: CertificateRevocationListInfo, indent: int = 0) -> None:
    print_key_oneline("Revocation List:", indent=indent)
    for revocation in crl_info["revoked_certificates"]:
        key = revocation["certificate_id"]
        print_key_value_oneline("Certificate ID:", key, indent=indent + 1)
        value = format_date_time(revocation["revocation_date"])
        print_key_value_oneline("Revocation Date:", value, indent=indent + 1)


def certificate_revocation_list_display(
    crl_info: CertificateRevocationListInfo,
) -> None:
    print_key_oneline("Certificate Revocation List:")

    visibility = get_element_visibility(".Data")
    if visibility != Visibility.HIDDEN:
        print_key_oneline("Data:", indent=1)

        visibility = get_element_visibility(".Signature.Algorithm")
        if visibility != Visibility.HIDDEN:
            key_style, value_style = get_key_value_styles(visibility)
            print_key_value_oneline(
                "Signature Algorithm:",
                OidNames[crl_info["signature_algorithm_oid"]].name,
                indent=2,
                key_style=key_style,
                value_style=value_style,
            )

        issuer_display(crl_info, indent=2)
        fingerprint_display(crl_info, indent=2)
        extensions_display(crl_info, indent=2)
        crl_display(crl_info, indent=2)

    visibility = get_element_visibility(".Signature")
    if visibility != Visibility.HIDDEN:
        signature_display(crl_info, indent=1)
