from typing import cast

from cryptography.x509.certificate_transparency import SignedCertificateTimestamp

from pkiviewer.model.extension.signed_certificate_timestamps import (
    SignedCertificateTimestampsInfo,
)
from pkiviewer.model.extension.precertificate_signed_certificate_timestamps import (
    PreCertificateSignedCertificateTimestampsInfo,
)
from pkiviewer.model import X509ExtensionInfo
from pkiviewer.view.formatter import (
    bytes_to_hex_long,
    format_date_time,
    format_version,
)
from pkiviewer.view.console import (
    print_key_oneline,
    print_key_value_oneline,
    print_hex_multiline,
)
from pkiviewer.view.theme import get_value_style, get_key_style
from pkiviewer.view.visibility import Visibility
from pkiviewer.context import _console  # type: ignore


def sct_display(
    sct: SignedCertificateTimestamp, indent: int, visibility: Visibility
) -> None:
    value_style = get_value_style(visibility)
    key_style = get_key_style(visibility)
    key_indent = indent
    value_indent = key_indent + 1
    print_key_oneline("Signed Certificate Timestamp:", key_indent, key_style=key_style)
    print_key_value_oneline(
        f"Version:",
        format_version(sct.version),
        value_indent,
        key_style=key_style,
        value_style=value_style,
    )
    log_id = bytes_to_hex_long(sct.log_id)
    print_key_oneline(f"Log ID:", value_indent, key_style=key_style)
    print_hex_multiline(
        log_id, indent=value_indent + 1, stride=16, value_style=value_style
    )
    print_key_value_oneline(
        "Timestamp:",
        format_date_time(sct.timestamp),
        value_indent,
        key_style=key_style,
        value_style=value_style,
    )


# RFC6962 3.3
def signed_certificate_timestamps_display(
    extension_info: X509ExtensionInfo,
    indent: int = 0,
    visibility: Visibility = Visibility.NORMAL,
) -> None:
    info = cast(SignedCertificateTimestampsInfo, extension_info["info"])
    for sct in info["timestamps"]:
        sct_display(sct, indent, visibility)


# RFC6962 3.3
def precertificate_signed_certificate_timestamps_display(
    extension_info: X509ExtensionInfo,
    indent: int = 0,
    visibility: Visibility = Visibility.NORMAL,
) -> None:
    info = cast(PreCertificateSignedCertificateTimestampsInfo, extension_info["info"])
    for sct in info["timestamps"]:
        sct_display(sct, indent, visibility)
