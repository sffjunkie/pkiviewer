from pkiviewer.context import _err_console  # type: ignore
from pkiviewer.types import X509Info
from pkiviewer.view.console import print_error, print_key_oneline, print_warning
from pkiviewer.view.theme import get_style


def report_display(info: X509Info) -> None:
    ec = _err_console.get()
    errors = info.get("errors", [])
    if errors:
        key_style = get_style("error")
        print_key_oneline("Errors:", key_style=key_style, c=ec)
        for error in errors:
            print_error(info["filename"], error, indent=1, c=ec)  # type: ignore

    warnings = info.get("warnings", [])
    if warnings:
        key_style = get_style("warning")
        print_key_oneline("Warnings:", key_style=key_style, c=ec)
        for warning in warnings:
            print_warning(info["filename"], warning, indent=1, c=ec)  # type: ignore
