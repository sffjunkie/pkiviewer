from cryptography.x509.extensions import AuthorityInformationAccess

from pkiviewer.model import (
    X509ExtensionTypeInfo,
    access_description_info,
    AccessDescriptionInfo,
)


# RFC5280 4.2.2.1
class AuthorityInformationAccessInfo(X509ExtensionTypeInfo):
    access_descriptions: list[AccessDescriptionInfo]


def authority_information_access_parse(
    extension: AuthorityInformationAccess,
) -> AuthorityInformationAccessInfo:
    access_descriptions: list[AccessDescriptionInfo] = []
    for description in extension._descriptions:  # type: ignore
        ad = access_description_info(description)
        access_descriptions.append(ad)

    ext_info: AuthorityInformationAccessInfo = {
        "type": "AuthorityInformationAccess",
        "access_descriptions": access_descriptions,
    }
    return ext_info
