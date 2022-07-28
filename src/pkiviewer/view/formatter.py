import datetime
from typing import Generator

from cryptography.x509 import Version as CertificateVersion
from cryptography.x509.certificate_transparency import (
    Version as CertificateTransparencyVersion,
)
import cryptography.x509.name


def _chunk(value: str, stride: int) -> Generator[str, None, None]:
    for idx in range(0, len(value), stride):
        yield value[idx : idx + stride]


def chunk(value: str, stride: int) -> list[str]:
    return list(_chunk(value, stride))


def hex_string_long(value: int) -> str:
    return int_to_hex_long(value)


def hex_string_split(value: str, octet_stride: int = 20) -> list[str]:
    return chunk(value, octet_stride * 3)


def int_to_hex_short(value: int) -> str:
    return f"{value} ({hex(value)})"


def int_to_hex_long(value: int) -> str:
    h = hex(value)[2:]

    if len(h) & 1 == 1:
        h = f"0{h}"

    elems = [h[x] + h[x + 1] for x in range(0, len(h), 2)]
    text = ":".join(elems)
    return text


def bytes_to_hex_long(sig: bytes | None = None) -> str:
    if sig is None:
        return ""

    hex_items = ["{:02x}".format(b) for b in sig]
    return ":".join(hex_items)


def format_date_time(dt: datetime.datetime) -> str:
    return dt.strftime("%b %d %H:%M:%S %Y") + " UTC"


def format_name(name: cryptography.x509.name.Name) -> str:
    def space_equals(text: str) -> str:
        return text.replace("=", " = ")

    n = name.rfc4514_string().split(",")
    n.reverse()
    n = [space_equals(e) for e in n]

    return ", ".join(n)


def format_version(version: CertificateVersion | CertificateTransparencyVersion):
    if version.v1:
        return "1 (0x0)"
    else:
        return "3 (0x2)"
