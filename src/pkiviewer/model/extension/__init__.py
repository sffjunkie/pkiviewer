from cryptography.x509.oid import ExtensionOID

from pkiviewer.model.extension.authority_key_identifier import (
    authority_key_identifier_parse,
)
from pkiviewer.model.extension.subject_key_identifier import (
    subject_key_identifier_parse,
)
from pkiviewer.model.extension.certificate_policy import certificate_policies_parse
from pkiviewer.model.extension.key_usage import key_usage_parse
from pkiviewer.model.extension.subject_alternative_name import (
    subject_alternative_name_parse,
)
from pkiviewer.model.extension.issuer_alternative_name import (
    issuer_alternative_name_parse,
)
from pkiviewer.model.extension.basic_constraints import basic_constraints_parse
from pkiviewer.model.extension.name_constraints import name_constraints_parse
from pkiviewer.model.extension.extended_key_usage import extended_key_usage_parse
from pkiviewer.model.extension.crl_distribution_points import (
    crl_distribution_points_parse,
)
from pkiviewer.model.extension.inhibit_any_policy import inhibit_any_policy_parse
from pkiviewer.model.extension.subject_information_access import (
    subject_information_access_parse,
)
from pkiviewer.model.extension.authority_information_access import (
    authority_information_access_parse,
)
from pkiviewer.model.extension.signed_certificate_timestamps import (
    signed_certificate_timestamps_parse,
)
from pkiviewer.model.extension.precertificate_signed_certificate_timestamps import (
    precertificate_signed_certificate_timestamps_parse,
)
from pkiviewer.model.extension.crl_number import crl_number_parse
from pkiviewer.model.extension.issuing_distribution_point import (
    issuing_distribution_point_parse,
)
from pkiviewer.model.extension.delta_crl_indicator import delta_crl_indicator_parse
from pkiviewer.model.extension.freshest_crl import freshest_crl_parse

v3_extension_parse = {
    # Certificate
    ExtensionOID.AUTHORITY_KEY_IDENTIFIER.dotted_string: authority_key_identifier_parse,
    ExtensionOID.SUBJECT_KEY_IDENTIFIER.dotted_string: subject_key_identifier_parse,
    ExtensionOID.KEY_USAGE.dotted_string: (key_usage_parse),
    ExtensionOID.CERTIFICATE_POLICIES.dotted_string: certificate_policies_parse,
    ExtensionOID.SUBJECT_ALTERNATIVE_NAME.dotted_string: subject_alternative_name_parse,
    ExtensionOID.ISSUER_ALTERNATIVE_NAME.dotted_string: issuer_alternative_name_parse,
    ExtensionOID.BASIC_CONSTRAINTS.dotted_string: basic_constraints_parse,
    ExtensionOID.NAME_CONSTRAINTS.dotted_string: name_constraints_parse,
    ExtensionOID.EXTENDED_KEY_USAGE.dotted_string: extended_key_usage_parse,
    ExtensionOID.CRL_DISTRIBUTION_POINTS.dotted_string: crl_distribution_points_parse,
    ExtensionOID.INHIBIT_ANY_POLICY.dotted_string: inhibit_any_policy_parse,
    ExtensionOID.AUTHORITY_INFORMATION_ACCESS.dotted_string: authority_information_access_parse,
    ExtensionOID.SUBJECT_INFORMATION_ACCESS.dotted_string: subject_information_access_parse,
    ExtensionOID.PRECERT_SIGNED_CERTIFICATE_TIMESTAMPS.dotted_string: precertificate_signed_certificate_timestamps_parse,
    ExtensionOID.SIGNED_CERTIFICATE_TIMESTAMPS.dotted_string: signed_certificate_timestamps_parse,
    ExtensionOID.CRL_NUMBER.dotted_string: crl_number_parse,
    ExtensionOID.DELTA_CRL_INDICATOR.dotted_string: delta_crl_indicator_parse,
    ExtensionOID.ISSUING_DISTRIBUTION_POINT.dotted_string: issuing_distribution_point_parse,
    ExtensionOID.FRESHEST_CRL.dotted_string: freshest_crl_parse,
    # Extensions not provided by the cryptography package
    # See https://github.com/pyca/cryptography/issues/1947
    ExtensionOID.POLICY_CONSTRAINTS.dotted_string: None,
    ExtensionOID.POLICY_MAPPINGS.dotted_string: None,
    ExtensionOID.SUBJECT_DIRECTORY_ATTRIBUTES: None,
    # Private Extensions
    "1.3.6.1.4.1.311.21.10": None,
    "1.3.6.1.4.1.311.21.7": None,
}
