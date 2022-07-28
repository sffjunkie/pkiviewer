from pkiviewer.context import _config  # type: ignore
from pkiviewer.types import Visibility


def get_element_visibility(
    element: str, default: Visibility | None = Visibility.NORMAL
) -> Visibility:
    c = _config.get()
    return c["visibility"].get(element, default)


def set_element_visibility(element: str, visibility: Visibility) -> None:
    c = _config.get()
    c["visibility"][element] = visibility


def get_extension_visibility(extension_id: str) -> Visibility:
    default_visibility = get_element_visibility(".Data.Extension")
    visibility = get_element_visibility(
        f".Data.Extension.{extension_id}", default=default_visibility
    )
    return visibility


def get_extension_value_visibility(extension_id: str) -> Visibility:
    default_visibility = get_element_visibility(".Data.Extension.Value")
    visibility = get_element_visibility(
        f".Data.Extension.{extension_id}.Value", default=default_visibility
    )
    return visibility
