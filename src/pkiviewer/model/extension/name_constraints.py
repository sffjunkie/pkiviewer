from typing import Any

from cryptography.x509.extensions import NameConstraints

from pkiviewer.model import X509ExtensionTypeInfo, general_names_parse


# RFC5280 4.2.1.10
class NameConstraintsInfo(X509ExtensionTypeInfo):
    permitted_subtrees: list[tuple[str, Any]]
    excluded_subtrees: list[tuple[str, Any]]


def name_constraints_parse(extension: NameConstraints) -> NameConstraintsInfo:
    permitted = general_names_parse(extension.permitted_subtrees)
    excluded = general_names_parse(extension.excluded_subtrees)

    ext_info: NameConstraintsInfo = {
        "type": "NameConstraints",
        "permitted_subtrees": permitted,
        "excluded_subtrees": excluded,
    }
    return ext_info
