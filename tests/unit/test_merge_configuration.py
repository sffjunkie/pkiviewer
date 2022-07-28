import pytest
from pkiviewer.config import merge, MergeError


def test_MergeEmptyConfigWithNonEmptyShouldPass():
    a = {}
    b = {"a": 1, "b": [1, 2, 3]}

    c = merge(a, b)

    assert c["a"] == 1
    assert c["b"] == [1, 2, 3]


def test_MergeNonEmptyConfigWithEmptyShouldPass():
    a = {"a": 1, "b": [1, 2, 3]}
    b = {}

    c = merge(a, b)

    assert c["a"] == 1
    assert c["b"] == [1, 2, 3]


def test_MergeValueWithValueShouldPass():
    a = {"b": 2}
    b = {"b": 4}

    c = merge(a, b)
    assert c["b"] == 4


def test_MergeValueWithListShouldFail():
    a = {"b": 2}
    b = {"b": [1, 2, 3]}

    with pytest.raises(MergeError):
        _c = merge(a, b)


def test_MergeValueWithDictShouldFail():
    a = {"b": 2}
    b = {"b": {"c": 1}}

    with pytest.raises(MergeError):
        _c = merge(a, b)


def test_MergeListWithValueShouldPass():
    a = {"b": [1, 2, 3]}
    b = {"b": 4}

    c = merge(a, b)
    assert c["b"] == [1, 2, 3, 4]


def test_MergeListWithListShouldPass():
    a = {"b": [1, 2, 3]}
    b = {"b": [4, 5, 6]}

    c = merge(a, b)
    assert c["b"] == [1, 2, 3, 4, 5, 6]


def test_MergeListWithDictShouldFail():
    a = {"b": [1, 2, 3]}
    b = {"b": {"c": 1}}

    with pytest.raises(MergeError):
        _c = merge(a, b)


def test_MergeDictWithValueShouldFail():
    a = {"b": {"c": 1}}
    b = {"b": 1}

    with pytest.raises(MergeError):
        _c = merge(a, b)


def test_MergeDictWithListShouldFail():
    a = {"b": {"c": 1}}
    b = {"b": [1, 2, 3]}

    with pytest.raises(MergeError):
        _c = merge(a, b)


def test_MergeDictWithDictSameTypesShouldPass():
    a = {"b": {"c": 1}}
    b = {"b": {"d": 2}}

    c = merge(a, b)
    assert c["b"] == {"c": 1, "d": 2}

    a = {"b": {"c": 1}}
    b = {"b": {"d": {"e": 2}}}

    c = merge(a, b)
    assert c["b"] == {"c": 1, "d": {"e": 2}}


def test_MergeDictWithDictDifferentTypesShouldFail():
    a = {"b": {"c": 1}}
    b = {"b": {"c": [1, 2, 3]}}

    with pytest.raises(MergeError):
        _c = merge(a, b)
