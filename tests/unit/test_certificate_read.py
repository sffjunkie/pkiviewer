from pathlib import Path
from cryptography.x509.base import Certificate

import pytest

from pkiviewer.view import rich_init
from pkiviewer.config import config_load
from pkiviewer.io import load
from pkiviewer.model.certificate import certiticate_parse


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
        _info = certiticate_parse(certificates[0], fullpath.name)
