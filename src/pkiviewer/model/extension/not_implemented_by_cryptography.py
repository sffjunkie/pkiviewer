from typing import TypedDict

from cryptography.x509.extensions import ExtensionType

from pkiviewer.model import X509ExtensionTypeInfo
from pkiviewer.oid import Oid

# NOTE: For the extensions in this module no information provided by the
# cryptography module
# See https://github.com/pyca/cryptography/issues/1947


# RFC5280 4.2.1.8
class SubjectDirectoryAttributesInfo(X509ExtensionTypeInfo):
    ...


def subject_directory_attributes_parse(
    extension: ExtensionType,
) -> SubjectDirectoryAttributesInfo:
    ...


# RFC5280 4.2.1.11
class PolicyConstraintsInfo(X509ExtensionTypeInfo):
    ...


def policy_constraints_parse(extension: ExtensionType) -> PolicyConstraintsInfo:
    ...


# RFC5280 4.2.1.5
class PolicyMapping(TypedDict):
    issuer_domain_policy: Oid
    subject_domain_policy: Oid


class PolicyMappingsInfo(X509ExtensionTypeInfo):
    policies: list[PolicyMapping]


def policy_mappings_parse(extension: ExtensionType) -> PolicyMappingsInfo:
    ...
