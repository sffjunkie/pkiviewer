from typing import cast

from cryptography import x509
from cryptography.x509.extensions import ExtensionType, IssuerAlternativeName

from pkiviewer.types import X509ExtensionTypeInfo


class IssuerAlternativeNameInfo(X509ExtensionTypeInfo):
    ians: dict[str, list[str]]


# RFC5280 4.2.1.7
def issuer_alternative_name_parse(
    extension: ExtensionType,
) -> IssuerAlternativeNameInfo:
    extension = cast(IssuerAlternativeName, extension)
    names = {
        x509.DNSName: "DNS",
        x509.RFC822Name: "email",
        x509.UniformResourceIdentifier: "URI",
        x509.IPAddress: "IP Address",
        x509.RegisteredID: "Registered ID",
    }
    ians: dict[str, list[str]] = {}
    for key, value in names.items():
        ian_list: list[str] = []
        for address in extension.get_values_for_type(key):  # type: ignore
            ian_list.append(str(address))
        if ian_list:
            ians[value] = ian_list
    ext_info: IssuerAlternativeNameInfo = {
        "type": "SubjectAlternativeName",
        "ians": ians,
    }
    return ext_info
