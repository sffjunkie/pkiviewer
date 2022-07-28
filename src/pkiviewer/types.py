from enum import Enum, auto
from typing import Any, TypedDict, Callable

from cryptography.x509.extensions import ExtensionType
from pkiviewer.model import X509ExtensionInfo
from pkiviewer.model import X509ExtensionTypeInfo


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


ExtensionParseMethod = Callable[[ExtensionType], X509ExtensionTypeInfo]
ExtensionDisplayMethod = Callable[[X509ExtensionInfo, int, Visibility], None]


class Error(TypedDict):
    module: str
    text: str


class Warning(TypedDict):
    module: str
    text: str
