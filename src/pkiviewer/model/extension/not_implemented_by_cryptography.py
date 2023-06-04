from typing import TypedDict

from cryptography.x509.extensions import UnrecognizedExtension

from pkiviewer.oid.names import Oid
from pkiviewer.types import X509ExtensionTypeInfo

# NOTE: For the extensions in this module no information provided by the
# cryptography module
# See https://github.com/pyca/cryptography/issues/1947


# RFC5280 4.2.1.8
class SubjectDirectoryAttributesInfo(X509ExtensionTypeInfo):
    ...


def subject_directory_attributes_parse(
    extension: UnrecognizedExtension,
) -> SubjectDirectoryAttributesInfo:
    ...


# RFC5280 4.2.1.11
class PolicyConstraintsInfo(X509ExtensionTypeInfo):
    ...


def policy_constraints_parse(extension: UnrecognizedExtension) -> PolicyConstraintsInfo:
    ...


# RFC5280 4.2.1.5
class PolicyMapping(TypedDict):
    issuer_domain_policy: Oid
    subject_domain_policy: Oid


class PolicyMappingsInfo(X509ExtensionTypeInfo):
    policies: list[PolicyMapping]


def policy_mappings_parse(extension: UnrecognizedExtension) -> PolicyMappingsInfo:
    ...
