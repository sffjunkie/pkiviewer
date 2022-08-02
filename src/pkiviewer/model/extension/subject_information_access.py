from typing import cast

from cryptography.x509.extensions import ExtensionType, SubjectInformationAccess

from pkiviewer.model import AccessDescriptionInfo, access_description_info
from pkiviewer.types import X509ExtensionTypeInfo


# RFC5280 4.2.2.2
class SubjectInformationAccessInfo(X509ExtensionTypeInfo):
    access_descriptions: list[tuple[str, str, str]]


def subject_information_access_parse(
    extension: ExtensionType,
) -> SubjectInformationAccessInfo:
    extension = cast(SubjectInformationAccess, extension)
    access_descriptions: list[AccessDescriptionInfo] = []
    for description in extension._descriptions:  # type: ignore
        ad = access_description_info(description)
        access_descriptions.append(ad)

    ext_info: SubjectInformationAccessInfo = {
        "type": "SubjectInformationAccess",
        "access_descriptions": access_descriptions,
    }
    return ext_info
