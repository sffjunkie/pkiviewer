from pkiviewer.config import Configuration, has_key


def test_config_has_key():
    d: Configuration = {"a": {"b": 2}}
    assert has_key("a", d)
    assert has_key("a.b", d)
    assert not has_key("a.b.c", d)

    d: Configuration = {"a": {"b": {"c": 3}}}
    assert has_key("a.b", d)
    assert has_key("a.b.c", d)

    assert not has_key("a.b.f", d)
