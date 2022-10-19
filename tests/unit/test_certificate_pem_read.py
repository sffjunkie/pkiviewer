from pathlib import Path

import pytest
from cryptography.x509.base import Certificate

from pkiviewer.config import config_load
from pkiviewer.io import load
from pkiviewer.model.certificate import certiticate_parse
from pkiviewer.view import rich_init


@pytest.mark.parametrize(
    "cert_file",
    ["microsoft.pem"],
)
def test_certificate_parsing(cert_file: str):
    config_load()
    rich_init()

    p = Path(__file__).parent
    fullpath = p / ".." / "file" / cert_file
    fullpath = fullpath.resolve()
    certificates = load(fullpath)
    if isinstance(certificates[0], Certificate):
        certiticate_parse(certificates[0], fullpath.name)
