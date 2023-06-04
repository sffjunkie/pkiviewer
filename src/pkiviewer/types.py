from enum import Enum, auto
from typing import Any, Callable, TypedDict

from cryptography.hazmat.primitives.serialization.pkcs12 import PKCS12KeyAndCertificates
from cryptography.x509 import (
    Certificate,
    CertificateRevocationList,
    CertificateSigningRequest,
)
from cryptography.x509.extensions import ExtensionType

from pkiviewer.oid.names import Oid


class Visibility(Enum):
    NORMAL = auto()
    HIDDEN = auto()
    HIGHLIGHT = auto()
    LOWLIGHT = auto()


CertificateSerialNumber = int


ConfigSection = dict[str, Any]


class Configuration(TypedDict):
    theme: ConfigSection
    visibility: ConfigSection
    output: ConfigSection


class Error(TypedDict):
    module: str
    text: str


class Warning(TypedDict):
    module: str
    text: str


X509Types = (
    Certificate
    | CertificateRevocationList
    | CertificateSigningRequest
    | PKCS12KeyAndCertificates
)


class X509ExtensionTypeInfo(TypedDict):
    type: str  # NOTE: type required as we can't use isinstance checks on a TypedDict


class X509ExtensionInfo(TypedDict):
    oid: Oid
    name: str
    critical: bool
    info: X509ExtensionTypeInfo


class X509Info(TypedDict):
    type: str
    filename: str
    errors: list[Error]
    warnings: list[Warning]


class PublicKeyInfo(TypedDict):
    type: str  # NOTE: type required as we can't use isinstance checks on a TypedDict
    name: str


ExtensionParseMethod = Callable[[ExtensionType], X509ExtensionTypeInfo]
ExtensionDisplayMethod = Callable[[X509ExtensionInfo, int, Visibility], None]
