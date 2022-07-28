from typing import cast

from cryptography.x509.certificate_transparency import SignedCertificateTimestamp
from cryptography.x509.extensions import (
    PrecertificateSignedCertificateTimestamps,
    ExtensionType,
)

from pkiviewer.model import X509ExtensionTypeInfo


class PreCertificateSignedCertificateTimestampsInfo(X509ExtensionTypeInfo):
    timestamps: list[SignedCertificateTimestamp]


# TODO Complete OreCertificateSignedCertificateTimestampsInfo
# entry_type: LogEntryType
# log_id: bytes
# timestamp: datetime.datetime
# version: Version
def precertificate_signed_certificate_timestamps_parse(
    extension: ExtensionType,
) -> PreCertificateSignedCertificateTimestampsInfo:
    ext = cast(PrecertificateSignedCertificateTimestamps, extension)
    # pb = ext.public_bytes()
    # print_hex_multiline(bytes_to_hex_long(pb), stride=16)
    # print("signed_certificate_timestamps_info")

    # decoder = asn1.Decoder()
    # decoder.start(pb)
    # elem: tuple[tuple[int, int, int], Any]
    # elem = decoder.read()
    # while elem is not None:
    #     tag, value = elem
    #     print(tag)
    #     print_hex_multiline(bytes_to_hex_long(value))
    #     elem = decoder.read()

    ext_info: PreCertificateSignedCertificateTimestampsInfo = {
        "type": "PreCertificateSignedCertificateTimestamps",
        "timestamps": ext._signed_certificate_timestamps[:],  # type: ignore
    }
    return ext_info
