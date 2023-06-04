from pkiviewer.oid.names import find_oid_or_parent


def test_find_id_that_exists():
    oid = "1.3.6.1.4.1.311.21.7"
    info = find_oid_or_parent(oid)
    assert info is not None
    assert info.name == "Microsoft szOID_CERTIFICATE_TEMPLATE"


def test_find_id_that_has_direct_parent():
    oid = "1.3.6.1.4.1.44947"
    info = find_oid_or_parent(oid)
    assert info is not None
    assert info.name == "IANA Private Enterprise Numbers"


def test_find_id_that_has_parent_in_tree():
    oid = "1.3.6.1.4.1.311.21.99"
    info = find_oid_or_parent(oid)
    assert info is not None
    assert info.name == "Microsoft PEN"
