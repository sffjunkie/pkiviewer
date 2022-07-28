from pkiviewer.config import has_key, Configuration


def test_config_has_key():
    d: Configuration = {"a": {"b": 2}}
    assert has_key("a", d) == True
    assert has_key("a.b", d) == True
    assert has_key("a.b.c", d) == False

    d: Configuration = {"a": {"b": {"c": 3}}}
    assert has_key("a.b", d) == True
    assert has_key("a.b.c", d) == True

    assert has_key("a.b.f", d) == False
