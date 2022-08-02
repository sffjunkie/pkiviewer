from typing import Any, cast

from cryptography.x509.extensions import ExtensionType, NameConstraints

from pkiviewer.model import general_names_parse
from pkiviewer.types import X509ExtensionTypeInfo


# RFC5280 4.2.1.10
class NameConstraintsInfo(X509ExtensionTypeInfo):
    permitted_subtrees: list[tuple[str, Any]]
    excluded_subtrees: list[tuple[str, Any]]


def name_constraints_parse(extension: ExtensionType) -> NameConstraintsInfo:
    extension = cast(NameConstraints, extension)
    permitted = general_names_parse(extension.permitted_subtrees)
    excluded = general_names_parse(extension.excluded_subtrees)

    ext_info: NameConstraintsInfo = {
        "type": "NameConstraints",
        "permitted_subtrees": permitted,
        "excluded_subtrees": excluded,
    }
    return ext_info
