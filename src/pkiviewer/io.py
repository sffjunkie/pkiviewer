import os
import io
import ssl
from pathlib import Path
from urllib.parse import urlparse
from cryptography.x509.base import Certificate
from cryptography.x509 import (
    CertificateRevocationList,
    CertificateSigningRequest,
    load_der_x509_certificate,
    load_der_x509_crl,
    load_der_x509_csr,
    load_pem_x509_certificate,
    load_pem_x509_crl,
    load_pem_x509_csr,
)
from cryptography.hazmat.primitives.serialization.pkcs12 import load_pkcs12
from rich.prompt import Prompt
from rich.text import Text
from pkiviewer.model import X509Types
from pkiviewer.context import _theme  # type: ignore


def download_pem(uri: str) -> list[X509Types]:
    elems = urlparse(uri, "https")
    cert = ssl.get_server_certificate((elems.netloc, 443))
    if cert:
        return [load_pem_x509_certificate(cert.encode("ascii"))]
    else:
        return []


def load_cer_der(data: bytes) -> Certificate:
    return load_der_x509_certificate(data)


def load_csr_der(data: bytes) -> CertificateSigningRequest:
    return load_der_x509_csr(data)


def load_crl_der(data: bytes) -> CertificateRevocationList:
    return load_der_x509_crl(data)


def load_cer_pem(lines: list[bytes]) -> Certificate:
    data = b"\n".join(lines)
    return load_pem_x509_certificate(data)


def load_crl_pem(lines: list[bytes]) -> CertificateRevocationList:
    data = b"\n".join(lines)
    return load_pem_x509_crl(data)


def load_csr_pem(lines: list[bytes]) -> CertificateSigningRequest:
    data = b"\n".join(lines)
    return load_pem_x509_csr(data)


def load_pem(pemfile: io.BufferedReader) -> list[X509Types]:
    items: list[X509Types] = []
    item_lines: list[bytes] = []
    in_cert = False
    in_crl = False
    in_csr = False
    lines = (line.strip() for line in pemfile)
    for line in lines:
        if not in_cert and line == b"-----BEGIN CERTIFICATE-----":
            in_cert = True
            item_lines.append(line)
        elif in_cert and line == b"-----END CERTIFICATE-----":
            item_lines.append(line)
            cer = load_cer_pem(item_lines)
            items.append(cer)
            item_lines = []
            in_cert = False
        elif not in_csr and line == b"-----BEGIN CERTIFICATE REQUEST-----":
            in_csr = True
            item_lines.append(line)
        elif in_csr and line == b"-----END CERTIFICATE REQUEST-----":
            item_lines.append(line)
            csr = load_csr_pem(item_lines)
            items.append(csr)
            item_lines = []
            in_csr = False
        elif not in_crl and line == b"-----BEGIN X509 CRL-----":
            in_crl = True
            item_lines.append(line)
        elif in_crl and line == b"-----END X509 CRL-----":
            item_lines.append(line)
            crl = load_crl_pem(item_lines)
            items.append(crl)
            item_lines = []
            in_cert = False
        else:
            item_lines.append(line)

    return items


def load_binary(
    data: bytes, filename: Path, password: str | None = None
) -> list[X509Types]:
    ext = filename.suffix
    if ext in [".cer", ".der"]:
        return [load_cer_der(data)]
    elif ext == ".csr":
        return [load_csr_der(data)]
    elif ext == ".crl":
        return [load_crl_der(data)]
    elif ext == ".p12":
        if password is not None:
            passwd = password.encode("ascii")
        else:
            passwd = password
        return [load_pkcs12(data, passwd)]
    else:
        return []


def load_ascii(fp: io.BufferedReader) -> list[X509Types]:
    certs = load_pem(fp)
    return certs


def load(filename: Path, password: str | None = None) -> list[X509Types]:
    with open(filename, mode="rb") as f:
        sig = f.read(4)
        f.seek(0, os.SEEK_SET)
        if sig == b"----":
            return load_ascii(f)
        else:
            data = f.read(-1)
            return load_binary(data, filename.absolute(), password=password)


def load_p12(p: Path) -> list[X509Types]:
    """Loads a PKCS#12 file and prompts for a password if required"""
    try:
        return load(p.resolve(), None)
    except ValueError:
        t = _theme.get()
        style = t.styles["info"]
        txt = Text(
            "Enter decryption password for P12 file or press Enter for no password",
            style=style,
        )
        passwd = Prompt.ask(
            txt,
            default=None,
            password=True,
        )
        return load(p.resolve(), passwd)
