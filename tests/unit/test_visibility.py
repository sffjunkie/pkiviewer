from pkiviewer.config import Configuration
from pkiviewer.view.visibility import (
    Visibility,
    get_element_visibility,
    set_element_visibility,
    get_extension_visibility,
    get_extension_value_visibility,
)


def test_element_visibility_is_normal(config: Configuration):
    assert get_element_visibility(".Header") == Visibility.NORMAL


def test_set_visibility(config: Configuration):
    set_element_visibility(".Header", Visibility.HIDDEN)
    assert get_element_visibility(".Header") == Visibility.HIDDEN


def test_extension_visibility_is_normal(config: Configuration):
    assert get_extension_visibility("SubjectKeyIdentifier") == Visibility.NORMAL


def test_extension_visibility_after_setting(config: Configuration):
    set_element_visibility(".Data.Extension.SubjectKeyIdentifier", Visibility.HIDDEN)
    assert get_extension_visibility("SubjectKeyIdentifier") == Visibility.HIDDEN


def test_extension_value_visibility_is_normal(config: Configuration):
    assert get_extension_value_visibility("SubjectKeyIdentifier") == Visibility.NORMAL


def test_extension_value_visibility_after_setting(config: Configuration):
    set_element_visibility(
        ".Data.Extension.SubjectKeyIdentifier.Value", Visibility.HIDDEN
    )
    assert get_extension_value_visibility("SubjectKeyIdentifier") == Visibility.HIDDEN
