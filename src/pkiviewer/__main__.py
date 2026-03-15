import os
from typing import Annotated
from pathlib import Path

import typer
from cryptography.hazmat.primitives.serialization.pkcs12 import PKCS12KeyAndCertificates
from cryptography.x509 import CertificateRevocationList, CertificateSigningRequest
from cryptography.x509.base import Certificate

from pkiviewer import __version__
from pkiviewer.config import config_load
from pkiviewer.context import _console  # type: ignore
from pkiviewer.io import download_pem, load, load_p12
from pkiviewer.model.certificate import certiticate_parse
from pkiviewer.model.crl import certiticate_revocation_list_parse

# from pkiviewer.model.csr import certificate_signing_request_parse
from pkiviewer.model.p12 import p12_key_and_certificates_parse
from pkiviewer.types import X509Types
from pkiviewer.utils import maybe
from pkiviewer.view import rich_init
from pkiviewer.view.console import print_info
from pkiviewer.view.display.certificate import certificate_display
from pkiviewer.view.display.common import report_display
from pkiviewer.view.display.crl import certificate_revocation_list_display

# from pkiviewer.view.display.csr import certificate_signing_request_display
from pkiviewer.view.display.p12 import p12_display


def _version_callback(value: bool) -> None:
    if value:
        print(f"pkiviewer {__version__}")
        raise typer.Exit()


def go(
    filename: Annotated[
        str,
        typer.Argument(help="Filename or url to display"),
    ],
    save_html: Annotated[
        Path | None,
        typer.Option("--save-html", help="Filename to save HTML to."),
    ] = None,
    save_svg: Annotated[
        Path | None,
        typer.Option("--save-svg", help="Filename to save SVG to."),
    ] = None,
    verbose: Annotated[
        bool,
        typer.Option("-v", "--verbose", help="Display more verbose ouput"),
    ] = False,
    width: Annotated[
        int,
        typer.Option(help="Number of columns to use when saving HTML/SVG"),
    ] = 100,
    version: Annotated[
        bool | None, typer.Option("--version", "-V", callback=_version_callback)
    ] = None,
):
    cfg = config_load()
    cfg["output"]["verbose"] = verbose

    if save_svg is None:
        output_svg = maybe(cfg, "output.svg", "")  # type: ignore
    else:
        output_svg = str(save_svg)

    if save_html is None:
        output_html = maybe(cfg, "output.html", "")  # type: ignore
    else:
        output_html = str(save_html)

    # Initialize rich
    if output_html or output_svg:
        record = True
        rich_init(
            record=record,
            file=open(os.devnull, "wt", encoding="utf-8"),
            color_system="truecolor",
            width=width,
        )
    else:
        record = False
        rich_init(record=False)

    info: list[X509Types]

    fname = str(filename)
    lcname = fname.lower()
    if lcname.startswith("https://") or lcname.startswith("http://"):
        info = download_pem(fname)
        if verbose:
            print_info(f"Downloading certificate from {fname}")
    else:
        x509_file_path = Path(fname)
        if x509_file_path.suffix == ".p12":
            info = load_p12(x509_file_path)
        else:
            info = load(x509_file_path.resolve())
        if verbose:
            print_info(f"Loading RFC5280 data from {x509_file_path.resolve()}")

    if info:
        element: X509Types | None
        for element in info:
            if element is None:
                continue

            if isinstance(element, Certificate):
                cert_info = certiticate_parse(element, fname)
                certificate_display(cert_info)
                report_display(cert_info)

            # TODO: Certificate Signing Request
            elif isinstance(element, CertificateSigningRequest):
                # csr_info = certificate_signing_request_parse(element, fname)
                # certificate_signing_request_display(csr_info)
                # report_display(csr_info)
                pass

            elif isinstance(element, CertificateRevocationList):  # type: ignore
                crl_info = certiticate_revocation_list_parse(element, fname)
                certificate_revocation_list_display(crl_info)
                report_display(crl_info)

            elif isinstance(element, PKCS12KeyAndCertificates):  # type: ignore
                p12_info = p12_key_and_certificates_parse(element, fname)
                p12_display(p12_info)
                report_display(p12_info)

    if record:
        clear = output_svg == ""
        con = _console.get()
        if output_svg:
            con.save_svg(output_svg, clear=clear)
        if output_html:
            con.save_html(output_html)


app = typer.run(go)
