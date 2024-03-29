from cryptography.hazmat.primitives.asymmetric.types import  PrivateKeyTypes
from cryptography.hazmat.primitives.serialization.pkcs12 import PKCS12KeyAndCertificates

from pkiviewer.model.certificate import CertificateInfo, certiticate_parse
from pkiviewer.types import X509Info


class PKCS12KeyAndCertificateInfo(X509Info):
    name: str
    certificate: CertificateInfo | None
    private_key:  PrivateKeyTypes | None
    additional_certs: list[CertificateInfo]


def p12_key_and_certificates_parse(
    p12: PKCS12KeyAndCertificates, filename: str
) -> PKCS12KeyAndCertificateInfo:
    cert_info: CertificateInfo | None = None
    if p12.cert:
        cert_info = certiticate_parse(p12.cert.certificate, filename)

    additional_cert_info: list[CertificateInfo] = []
    for additional_cert in p12.additional_certs:
        additional_cert_info.append(
            certiticate_parse(additional_cert.certificate, filename)
        )

    info: PKCS12KeyAndCertificateInfo = {
        "type": "p12",
        "filename": filename,
        "name": "PKCS12KeyAndCertificate",
        "certificate": cert_info,
        "private_key": p12.key,
        "additional_certs": additional_cert_info,
        "errors": [],
        "warnings": [],
    }

    return info
