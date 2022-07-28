from typing import cast

from cryptography.x509.certificate_transparency import SignedCertificateTimestamp
from cryptography.x509.extensions import SignedCertificateTimestamps, ExtensionType

from pkiviewer.model import X509ExtensionTypeInfo


class SignedCertificateTimestampsInfo(X509ExtensionTypeInfo):
    timestamps: list[SignedCertificateTimestamp]


# TODO Complete SignedCertificateTimestampsInfo
# entry_type: LogEntryType
# log_id: bytes
# timestamp: datetime.datetime
# version: Version
def signed_certificate_timestamps_parse(
    extension: ExtensionType,
) -> SignedCertificateTimestampsInfo:
    ext = cast(SignedCertificateTimestamps, extension)
    # pb = ext.public_bytes()
    # print_hex_multiline(bytes_to_hex_long(pb), stride=16)
    # print("signed_certificate_timestamps_info")

    ext_info: SignedCertificateTimestampsInfo = {
        "type": "Signed Certificate Timestamps",
        "timestamps": ext._signed_certificate_timestamps[:],  # type: ignore
    }
    return ext_info
