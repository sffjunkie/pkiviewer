import os
from pathlib import Path

import click

from pkiviewer.config import config_load
from pkiviewer.io import load, download_pem, load_p12
from pkiviewer.model import X509Types
from pkiviewer.view import rich_init
from pkiviewer.view.console import print_info
from pkiviewer.utils import maybe
from pkiviewer.context import _console, _config  # type: ignore

from cryptography.x509.base import Certificate
from pkiviewer.model.certificate import certiticate_parse
from pkiviewer.view.display.certificate import (
    certificate_display,
    certificate_report_display,
)

# from cryptography.x509 import CertificateSigningRequest
# from pkiviewer.model.csr import certificate_signing_request_parse
# from pkiviewer.ui.rich.output.csr import certificate_signing_request_display

# from cryptography.x509 import CertificateRevocationList
# from pkiviewer.model.crl import certiticate_revocation_list_parse
# from pkiviewer.ui.rich.output.crl import certificate_signing_request_display

from cryptography.hazmat.primitives.serialization.pkcs12 import PKCS12KeyAndCertificates
from pkiviewer.model.p12 import p12_key_and_certificates_parse
from pkiviewer.view.display.p12 import p12_display

__version__ = "0.1.1"
__author__ = "Simon Kennedy <sffjunkie+code@gmail.com>"

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("filename", type=click.Path())
@click.option(
    "--save-html",
    type=click.Path(),
    help="Filename to save HTML to.",
    metavar="HTMLFILE",
)
@click.option(
    "--save-svg", type=click.Path(), help="Filename to save SVG to.", metavar="SVGFILE"
)
@click.option("-v", "--verbose", is_flag=True, help="Display more ouput")
@click.option(
    "--width",
    default=100,
    help="Number of columns to use when saving HTML/SVG",
    show_default=True,
)
@click.version_option(__version__, "--version", "-V", prog_name="pkiviewer")
def run(
    filename: click.Path,
    save_html: click.Path | None,
    save_svg: click.Path | None,
    verbose: bool,
    width: int,
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
            file=open(os.devnull, "wt"),
            color_system="truecolor",
            width=width,
        )
    else:
        record = False
        rich_init(record=False)

    con = _console.get()

    info: list[X509Types]

    fname = str(filename)
    lcname = fname.lower()
    if lcname.startswith("https://") or lcname.startswith("http://"):
        info = download_pem(fname)
        if verbose:
            print_info(f"Downloading certificate from {fname}")
    else:
        p = Path(fname)
        if p.suffix == ".p12":
            info = load_p12(p)
        else:
            info = load(p.resolve())
        if verbose:
            print_info(f"Loading RFC5280 data from {p.resolve()}")

    if info:
        element: X509Types | None
        for element in info:
            if element is None:
                continue

            if isinstance(element, Certificate):
                cert_info = certiticate_parse(element, fname)
                certificate_display(cert_info)
                certificate_report_display(cert_info)

            # TODO: Certificate Signing Request
            # elif isinstance(element, CertificateSigningRequest):
            #     csr_info = certificate_signing_request_parse(element, fname)
            #     certificate_signing_request_display(csr_info)

            # TODO: Certificate Revocation List
            # elif isinstance(element, CertificateRevocationList):  # type: ignore
            #     crl_info = certiticate_revocation_list_parse(element, fname)

            elif isinstance(element, PKCS12KeyAndCertificates):  # type: ignore
                p12_info = p12_key_and_certificates_parse(element, fname)
                p12_display(p12_info)

    if record:
        clear = output_svg == ""
        if output_svg:
            con.save_svg(output_svg, clear=clear)
        if output_html:
            con.save_html(output_html)


run()
