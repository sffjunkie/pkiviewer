from typing import Any

from cryptography.x509.extensions import Extensions, ExtensionType, Extension

from pkiviewer.oid import Oid, OidNames
from pkiviewer.model.extension import v3_extension_parse


def get_extension_for_oid(
    extensions: Extensions, oid: Oid
) -> Extension[ExtensionType] | None:
    for e in extensions:
        if e.oid.dotted_string == oid:
            return e

    return None


SortedExtensionInfo = tuple[str, Any, str]


def sort_extensions_by_rfc_section(extensions: Extensions) -> list[SortedExtensionInfo]:
    def _section_to_key(section: SortedExtensionInfo) -> str:
        if section[0] is None:
            return "Z"

        rfc, s = section[0].split(" ")
        s = rfc + "".join([f"{int(e):02d}" for e in s.split(".")])
        return s

    a = [
        (
            OidNames[ext.oid.dotted_string].defined_in,
            v3_extension_parse[ext.oid.dotted_string],
            ext.oid.dotted_string,
        )
        for ext in extensions
        if ext.oid.dotted_string in v3_extension_parse
    ]
    result: list[SortedExtensionInfo] = sorted(a, key=_section_to_key)  # type: ignore
    return result
