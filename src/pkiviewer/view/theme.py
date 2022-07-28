import rich.style

from pkiviewer.context import _theme  # type: ignore
from pkiviewer.view.color import brighten
from pkiviewer.view.visibility import Visibility


def get_style(key: str) -> rich.style.Style:
    t = _theme.get()
    if key in t.styles:
        return t.styles[key]
    else:
        return t.styles["default"]


def get_key_style(visibility: Visibility) -> rich.style.Style:
    if visibility == Visibility.LOWLIGHT:
        key_style = get_style("key")
        key_style = rich.style.Style(color=key_style.color, dim=True)
    elif visibility == Visibility.HIGHLIGHT:
        key_style = get_style("key")
        key_style = rich.style.Style.from_color(brighten(key_style.color))
    else:
        key_style = get_style("key")

    return key_style


def get_value_style(visibility: Visibility) -> rich.style.Style:
    if visibility == Visibility.LOWLIGHT:
        value_style = get_style("key")
        value_style = rich.style.Style(color=value_style.color, dim=True)
    elif visibility == Visibility.HIGHLIGHT:
        value_style = get_style("value")
        value_style = rich.style.Style.from_color(brighten(value_style.color))
    else:
        value_style = get_style("value")

    return value_style


def get_key_value_styles(
    visibility: Visibility,
) -> tuple[rich.style.Style, rich.style.Style]:
    return get_key_style(visibility), get_value_style(visibility)


def get_link_style(visibility: Visibility, url: str) -> rich.style.Style:
    value_style = get_value_style(visibility)
    link_style = rich.style.Style(link=f"link {url}")
    return value_style + link_style


INDENTS = 10
INDENT_PER_LEVEL = 4
indents = [" " * INDENT_PER_LEVEL * x for x in range(INDENTS)]
