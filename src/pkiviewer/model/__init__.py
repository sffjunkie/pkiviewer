from typing import Any, TypedDict

from cryptography.x509.extensions import AccessDescription
from cryptography.x509.general_name import GeneralName
from cryptography.x509.name import RelativeDistinguishedName

from pkiviewer.oid.names import OidNames

GeneralNameInfo = tuple[str, Any]

GeneralNameToShortName: dict[str, str] = {  # type: ignore
    "DNSName": "DNS",
    "UniformResourceIdentifier": "URI",
    "RFC822Name": "email",
    "DirectoryName": "DirectoryName",
    "IPAddress": "IP",
}


class DistributionPointInfo(TypedDict):
    names: list[GeneralNameInfo]
    reasons: list[str]
    crl_issuer: list[GeneralNameInfo]


def general_name_parse(
    name: GeneralName,
) -> str:
    def _lookup_name(instance: GeneralName) -> str:
        short_name = GeneralNameToShortName.get(instance.__class__.__name__, None)
        if short_name is not None:
            return short_name
        else:
            return f"Unknown GeneralName {instance.__class__.__name__}"

    return _lookup_name(name)


def general_names_parse(
    names: list[GeneralName] | None,
) -> list[GeneralNameInfo]:
    if names is None:
        return []

    return [(general_name_parse(name), name.value) for name in names]


def relative_distinguished_names_parse(
    dpi: RelativeDistinguishedName,
) -> list[GeneralNameInfo]:
    names: list[GeneralNameInfo] = []
    if dpi is not None:
        return [("RDN", name.rfc4514_string()) for name in dpi]
        for name in dpi:
            names.append(("RDN", name.rfc4514_string()))

    return names


AccessDescriptionInfo = tuple[str, str, str]


def access_description_info(description: AccessDescription) -> AccessDescriptionInfo:
    access_method = OidNames[description.access_method.dotted_string].name
    access_type = general_name_parse(description.access_location)
    access_location = description.access_location.value
    return (access_method, access_type, access_location)
