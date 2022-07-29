from cryptography.x509 import DNSName, RFC822Name
from pkiviewer.model import general_name_parse


def test_GeneralName_Lookup():
    assert general_name_parse(DNSName("a")) == "DNS"
    assert general_name_parse(RFC822Name("a")) == "email"
