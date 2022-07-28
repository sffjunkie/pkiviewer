import textwrap
from typing import Any

import rich.console
import rich.style
import rich.theme

from pkiviewer.types import Warning, Error
from pkiviewer.view.theme import indents, INDENT_PER_LEVEL, get_style
from pkiviewer.view.formatter import int_to_hex_short, hex_string_split
from pkiviewer.context import _console  # type: ignore

MAX_STRIDE = 24


def print_info(text: str, indent: int = 0) -> None:
    c = _console.get()
    c.print(f"{indents[indent]}[info]{text}[/]", emoji=False, highlight=False)


def print_hex_oneline(
    value: int,
    indent: int = 0,
    value_style: rich.style.Style | None = None,
) -> None:
    c = _console.get()
    text = int_to_hex_short(value)
    c.print(f"{indents[indent]}[{value_style}]{text}[/]", emoji=False, highlight=False)


def print_hex_multiline(
    hex_str: str,
    indent: int = 0,
    stride: int = -1,
    value_style: rich.style.Style | None = None,
) -> None:
    c = _console.get()
    width = c.width

    max_stride = (width - len(indents[indent])) // 3
    max_stride = max_stride if max_stride < MAX_STRIDE else MAX_STRIDE

    stride = stride if stride != -1 and stride < max_stride else max_stride

    if value_style is None:
        value_style = get_style("value")
    hex_strings = hex_string_split(hex_str, stride)
    hex_strings_indented = [f"{indents[indent]}{s}" for s in hex_strings]
    text = "\n".join(hex_strings_indented)
    c.print(f"[{value_style}]{text}[/]", emoji=False, highlight=False)


def print_key_oneline(
    key: str,
    indent: int = 0,
    key_style: rich.style.Style | None = None,
) -> None:
    c = _console.get()
    if key_style is None:
        key_style = get_style("key")
    c.print(f"{indents[indent]}[{key_style}]{key}[/]", emoji=False, highlight=False)


def print_value_oneline(
    value: str,
    indent: int = 0,
    value_style: rich.style.Style | None = None,
) -> None:
    c = _console.get()
    if value_style is None:
        value_style = get_style("value")
    c.print(f"{indents[indent]}[{value_style}]{value}[/]", emoji=False, highlight=False)


def print_value_multiline(
    value: str,
    indent: int = 0,
    value_style: rich.style.Style | None = None,
) -> None:
    if value_style is None:
        value_style = get_style("value")

    c = _console.get()
    space_left = c.width - indent * INDENT_PER_LEVEL
    if space_left < len(value):
        text = textwrap.fill(
            value,
            width=c.width,
            initial_indent=indents[indent],
            subsequent_indent=indents[indent],
        )
        c.print(f"[{value_style}]{text}[/]", emoji=False, highlight=False)
    else:
        print_value_oneline(f"[{value_style}]{value}[/]", indent=indent)


def print_multivalue_multiline(
    value: list[str],
    indent: int = 0,
    value_style: rich.style.Style | None = None,
) -> None:
    for item in value:
        print_value_multiline(item, indent=indent, value_style=value_style)


def print_key_value_oneline(
    key: str,
    value: Any,
    indent: int = 0,
    key_style: rich.style.Style | None = None,
    value_style: rich.style.Style | None = None,
) -> None:
    c = _console.get()
    if key_style is None or value_style is None:
        if key_style is None:
            key_style = get_style("key")
        if value_style is None:
            value_style = get_style("value")

    c.print(
        f"{indents[indent]}[{key_style}]{key}[/] [{value_style}]{value}[/]",
        emoji=False,
        highlight=False,
    )


def print_key_value_multiline(
    key: str,
    value: Any,
    indent: int = 0,
    key_style: rich.style.Style | None = None,
    value_style: rich.style.Style | None = None,
) -> None:
    if key_style is None or value_style is None:
        if key_style is None:
            key_style = get_style("key")
        if value_style is None:
            value_style = get_style("value")

    print_key_oneline(key, indent, key_style)
    print_value_multiline(value, indent + 1, value_style)


def print_error(filename: str, error: Error, indent: int = 0):
    c = _console.get()
    c.print(f"{indents[indent]}[error]{filename}[/]", highlight=False)

    text = f"{error['module']}: {error['text']}"
    text = textwrap.fill(
        text,
        width=c.width,
        initial_indent=indents[indent + 1],
        subsequent_indent=indents[indent + 1],
    )
    c.print(f"[error]{text}[/]", highlight=False)


def print_warning_text(text: str):
    c = _console.get()
    c.print(f"[warning]{text}[/]", highlight=False)


def print_warning(filename: str, warning: Warning, indent: int = 0):
    c = _console.get()
    c.print(f"{indents[indent]}[warning]{filename}[/]", highlight=False)

    text = f"{warning['module']}: {warning['text']}"
    text = textwrap.fill(
        text,
        width=c.width,
        initial_indent=indents[indent + 1],
        subsequent_indent=indents[indent + 1],
    )
    c.print(f"[warning]{text}[/]", highlight=False)
