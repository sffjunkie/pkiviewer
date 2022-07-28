from pkiviewer.model import X509ExtensionInfo
from pkiviewer.view.visibility import Visibility

# NOTE: No information provided by the cryptography module for these extensions
# See https://github.com/pyca/cryptography/issues/1947


# RFC5280 4.2.1.11
def policy_constraints_display(
    extension_info: X509ExtensionInfo,
    indent: int = 0,
    visibility: Visibility = Visibility.NORMAL,
):
    ...


# RFC5280 4.2.1.8
def subject_directory_attributes_display(
    extension_info: X509ExtensionInfo,
    indent: int = 0,
    visibility: Visibility = Visibility.NORMAL,
):
    ...


# RFC5280 4.2.1.5
def policy_mappings_display(
    extension_info: X509ExtensionInfo,
    indent: int = 0,
    visibility: Visibility = Visibility.NORMAL,
) -> None:
    ...
