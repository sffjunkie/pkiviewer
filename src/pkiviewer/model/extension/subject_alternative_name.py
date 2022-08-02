from typing import Type, cast

from cryptography.x509.extensions import ExtensionType, SubjectAlternativeName
from cryptography.x509.general_name import (
    DNSName,
    RFC822Name,
    UniformResourceIdentifier,
)

from pkiviewer.types import X509ExtensionTypeInfo


# RFC5280 4.2.1.6
class SubjectAlternativeNameInfo(X509ExtensionTypeInfo):
    sans: dict[str, list[str]]


GeneralNameToShortName: dict[
    Type[DNSName] | Type[UniformResourceIdentifier] | Type[RFC822Name], str
] = {
    DNSName: "DNS",
    UniformResourceIdentifier: "URI",
    RFC822Name: "email",
}


def subject_alternative_name_parse(
    extension: ExtensionType,
) -> SubjectAlternativeNameInfo:
    extension = cast(SubjectAlternativeName, extension)
    sans: dict[str, list[str]] = {}
    for key, value in GeneralNameToShortName.items():
        san_list: list[str] = []
        for address in extension.get_values_for_type(key):
            san_list.append(str(address))
        if san_list:
            sans[value] = san_list

    ext_info: SubjectAlternativeNameInfo = {
        "type": "SubjectAlternativeName",
        "sans": sans,
    }
    return ext_info
