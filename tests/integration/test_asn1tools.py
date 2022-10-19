import pytest

from pkiviewer.asn1.load_specification import load_asn1_specification


@pytest.mark.skip(reason="asn1tools does not support CLASS")
def test_LoadASN1Grammar():
    spec_file = "future/PKIX-CommonTypes-2009.asn1"
    load_asn1_specification(spec_file)
