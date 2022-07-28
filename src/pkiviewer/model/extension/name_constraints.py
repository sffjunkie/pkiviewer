from typing import cast, Any

from cryptography.x509.extensions import NameConstraints, ExtensionType

from pkiviewer.model import X509ExtensionTypeInfo, general_names_parse


# RFC5280 4.2.1.10
class NameConstraintsInfo(X509ExtensionTypeInfo):
    permitted_subtrees: list[tuple[str, Any]]
    excluded_subtrees: list[tuple[str, Any]]


def name_constraints_parse(extension: ExtensionType) -> NameConstraintsInfo:
    ext = cast(NameConstraints, extension)

    permitted = general_names_parse(ext.permitted_subtrees)
    excluded = general_names_parse(ext.excluded_subtrees)

    ext_info: NameConstraintsInfo = {
        "type": "NameConstraints",
        "permitted_subtrees": permitted,
        "excluded_subtrees": excluded,
    }
    return ext_info
