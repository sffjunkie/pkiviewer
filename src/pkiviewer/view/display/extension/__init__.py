from cryptography.x509.oid import ExtensionOID

from pkiviewer.oid import Oid
from pkiviewer.types import ExtensionDisplayMethod


from pkiviewer.view.display.extension.authority_information_access import (
    authority_information_access_display,
)
from pkiviewer.view.display.extension.authority_key_identifier import (
    authority_key_identifier_display,
)
from pkiviewer.view.display.extension.basic_constraints import (
    basic_constraints_display,
)
from pkiviewer.view.display.extension.certificate_policies import (
    certificate_policies_display,
)
from pkiviewer.view.display.extension.crl_distribution_ponts import (
    crl_distribution_points_display,
)
from pkiviewer.view.display.extension.extended_key_usage import (
    extended_key_usage_display,
)
from pkiviewer.view.display.extension.issuer_alternative_name import (
    issuer_alternative_name_display,
)
from pkiviewer.view.display.extension.key_usage import key_usage_display
from pkiviewer.view.display.extension.signed_certificate_timestamps import (
    signed_certificate_timestamps_display,
    precertificate_signed_certificate_timestamps_display,
)
from pkiviewer.view.display.extension.subject_alternative_name import (
    subject_alternative_name_display,
)
from pkiviewer.view.display.extension.subject_information_access import (
    subject_information_access_display,
)
from pkiviewer.view.display.extension.subject_key_identifier import (
    subject_key_identifier_display,
)
from pkiviewer.view.display.extension.not_implemented_by_cryptography import (
    policy_mappings_display,
)
from pkiviewer.view.display.extension.not_implemented_by_cryptography import (
    subject_directory_attributes_display,
)
from pkiviewer.view.display.extension.name_constraints import (
    name_constraints_display,
)
from pkiviewer.view.display.extension.not_implemented_by_cryptography import (
    policy_constraints_display,
)
from pkiviewer.view.display.extension.inhibit_any_policy import (
    inhibit_any_policy_display,
)
from pkiviewer.view.display.extension.freshest_crl_display import (
    freshest_crl_display,
)


v3_extension_display: dict[Oid, ExtensionDisplayMethod] = {
    # RFC5280
    ExtensionOID.AUTHORITY_INFORMATION_ACCESS.dotted_string: authority_information_access_display,
    ExtensionOID.AUTHORITY_KEY_IDENTIFIER.dotted_string: authority_key_identifier_display,
    ExtensionOID.BASIC_CONSTRAINTS.dotted_string: basic_constraints_display,
    ExtensionOID.CERTIFICATE_POLICIES.dotted_string: certificate_policies_display,
    ExtensionOID.CRL_DISTRIBUTION_POINTS.dotted_string: crl_distribution_points_display,
    ExtensionOID.EXTENDED_KEY_USAGE.dotted_string: extended_key_usage_display,
    ExtensionOID.ISSUER_ALTERNATIVE_NAME.dotted_string: issuer_alternative_name_display,
    ExtensionOID.KEY_USAGE.dotted_string: key_usage_display,
    ExtensionOID.SIGNED_CERTIFICATE_TIMESTAMPS.dotted_string: signed_certificate_timestamps_display,
    ExtensionOID.SUBJECT_ALTERNATIVE_NAME.dotted_string: subject_alternative_name_display,
    ExtensionOID.SUBJECT_INFORMATION_ACCESS.dotted_string: subject_information_access_display,
    ExtensionOID.SUBJECT_KEY_IDENTIFIER.dotted_string: subject_key_identifier_display,
    ExtensionOID.POLICY_MAPPINGS.dotted_string: policy_mappings_display,
    ExtensionOID.SUBJECT_DIRECTORY_ATTRIBUTES.dotted_string: subject_directory_attributes_display,
    ExtensionOID.NAME_CONSTRAINTS.dotted_string: name_constraints_display,
    ExtensionOID.POLICY_CONSTRAINTS.dotted_string: policy_constraints_display,
    ExtensionOID.INHIBIT_ANY_POLICY.dotted_string: inhibit_any_policy_display,
    ExtensionOID.FRESHEST_CRL.dotted_string: freshest_crl_display,
    # RFC6962
    ExtensionOID.SIGNED_CERTIFICATE_TIMESTAMPS.dotted_string: signed_certificate_timestamps_display,
    ExtensionOID.PRECERT_SIGNED_CERTIFICATE_TIMESTAMPS.dotted_string: precertificate_signed_certificate_timestamps_display,
    # Private Extensions
    # "1.3.6.1.4.1.311.21.10": None,
    # "1.3.6.1.4.1.311.21.7": None,
}
