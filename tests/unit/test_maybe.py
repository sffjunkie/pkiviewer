from pkiviewer.utils import maybe


def test_maybe_should_return_a_value():
    d = {"a": {"b": {"c": 3}}}
    assert maybe(d, "a.b.c") == 3
    assert maybe(d, "a.b") == {"c": 3}
    assert maybe(d, "a") == {"b": {"c": 3}}


def test_maybe_should_return_none():
    d = {"a": {"b": {"c": 3}}}
    assert maybe(d, "a.b.e") is None
    assert maybe(d, "c") == None
