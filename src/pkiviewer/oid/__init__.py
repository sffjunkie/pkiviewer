"""OID to name mappings"""

from typing import NamedTuple

from cryptography.x509.oid import (
    AuthorityInformationAccessOID,
    ExtendedKeyUsageOID,
    ExtensionOID,
    SignatureAlgorithmOID,
    NameOID,
)
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurveOID


Oid = str
OidName = str


class OidInfo(NamedTuple):
    name: OidName
    defined_in: str | None


OidDatabase = dict[Oid, OidInfo]


OidNames: OidDatabase = {
    # region Name OIDs
    NameOID.BUSINESS_CATEGORY.dotted_string: OidInfo(
        "Business Category", "ITU-T X.520, RFC4519 2.1"
    ),
    NameOID.COMMON_NAME.dotted_string: OidInfo(
        "Common Name", "ITU-T X.520, RFC4519 2.3"
    ),
    NameOID.COUNTRY_NAME.dotted_string: OidInfo(
        "Country Name", "ITU-T X.520, RFC4519 2.2"
    ),
    NameOID.DN_QUALIFIER.dotted_string: OidInfo(
        "DN Qualifier", "ITU-T X.520, RFC4519 2.8"
    ),
    NameOID.DOMAIN_COMPONENT.dotted_string: OidInfo("Domain Component", "RFC1274"),
    NameOID.EMAIL_ADDRESS.dotted_string: OidInfo("Email Address", "RFC2985 B.3.5"),
    NameOID.GENERATION_QUALIFIER.dotted_string: OidInfo(
        "Generation Qualifier", "ITU-T X.520, RFC4519 2.11"
    ),
    NameOID.GIVEN_NAME.dotted_string: OidInfo(
        "Given Name", "ITU-T X.520, RFC4519 2.12"
    ),
    NameOID.INN.dotted_string: OidInfo("Individual Taxpayer Number", "RFC9215 5.1"),
    NameOID.JURISDICTION_COUNTRY_NAME.dotted_string: OidInfo(
        "Jurisdiction Country Name",
        None,
    ),
    NameOID.JURISDICTION_LOCALITY_NAME.dotted_string: OidInfo(
        "Jurisdiction Locality Name",
        None,
    ),
    NameOID.JURISDICTION_STATE_OR_PROVINCE_NAME.dotted_string: OidInfo(
        "Jurisdiction State Or Province",
        None,
    ),
    NameOID.LOCALITY_NAME.dotted_string: OidInfo(
        "Locality", "ITU-T X.520, RFC4519 3.7"
    ),
    NameOID.STATE_OR_PROVINCE_NAME.dotted_string: OidInfo(
        "State Or Province", "ITU-T X.520, RFC4519 2.33"
    ),
    NameOID.STREET_ADDRESS.dotted_string: OidInfo(
        "Street Address", "ITU-T X.520, RFC4519 2.34"
    ),
    NameOID.ORGANIZATION_NAME.dotted_string: OidInfo(
        "Organization Name", "ITU-T X.521, RFC4519 3.8"
    ),
    NameOID.ORGANIZATIONAL_UNIT_NAME.dotted_string: OidInfo(
        "Organizational Unit Name", "ITU-T X.521, RFC4519 3.11"
    ),
    NameOID.SERIAL_NUMBER.dotted_string: OidInfo(
        "Serial Number", "ITU-T X.520, RFC4519 2.31"
    ),
    NameOID.SURNAME.dotted_string: OidInfo("Surname", "ITU-T X.520, RFC4519 2.32"),
    NameOID.TITLE.dotted_string: OidInfo("Title", "ITU-T X.520, RFC4519 2.38"),
    NameOID.X500_UNIQUE_IDENTIFIER.dotted_string: OidInfo(
        "X500 Unique Identifier", "ITU-T X.520, RFC4519 2.43"
    ),
    NameOID.PSEUDONYM.dotted_string: OidInfo("Pseudonym", "ITU-T X.520, RFC2985 5.2.9"),
    NameOID.USER_ID.dotted_string: OidInfo("User ID", "RFC1274"),
    NameOID.POSTAL_ADDRESS.dotted_string: OidInfo("Postal Address", None),
    NameOID.POSTAL_CODE.dotted_string: OidInfo("Postal Code", None),
    NameOID.OGRN.dotted_string: OidInfo("OGRN", None),
    NameOID.SNILS.dotted_string: OidInfo("SNILS", None),
    NameOID.UNSTRUCTURED_NAME.dotted_string: OidInfo("Unstructured Name", None),
    # endregion
    # region Authority Information Access OIDs
    AuthorityInformationAccessOID.CA_ISSUERS.dotted_string: OidInfo("CA Issuers", None),
    AuthorityInformationAccessOID.OCSP.dotted_string: OidInfo("OCSP", None),
    # endregion
    # region Extended Key Usage OIDs
    ExtendedKeyUsageOID.CLIENT_AUTH.dotted_string: OidInfo(
        "TLS Web Client Authentication",
        None,
    ),
    ExtendedKeyUsageOID.CODE_SIGNING.dotted_string: OidInfo("Code Signing", None),
    ExtendedKeyUsageOID.EMAIL_PROTECTION.dotted_string: OidInfo(
        "E-mail Protection", None
    ),
    ExtendedKeyUsageOID.KERBEROS_PKINIT_KDC.dotted_string: OidInfo(
        "Kerboros PKINIT KDC",
        None,
    ),
    ExtendedKeyUsageOID.OCSP_SIGNING.dotted_string: OidInfo("OCSP Signing", None),
    ExtendedKeyUsageOID.SERVER_AUTH.dotted_string: OidInfo(
        "TLS Web Server Authentication",
        None,
    ),
    ExtendedKeyUsageOID.SMARTCARD_LOGON.dotted_string: OidInfo("Smartcard Login", None),
    ExtendedKeyUsageOID.TIME_STAMPING.dotted_string: OidInfo("Time Stamping", None),
    # endregion
    # region Extension OIDs
    ExtensionOID.AUTHORITY_INFORMATION_ACCESS.dotted_string: OidInfo(
        "Authority Information Access",
        "RFC5280 4.2.2.1",
    ),
    ExtensionOID.AUTHORITY_KEY_IDENTIFIER.dotted_string: OidInfo(
        "Authority Key Identifier",
        "RFC5280 4.2.1.1",
    ),
    ExtensionOID.BASIC_CONSTRAINTS.dotted_string: OidInfo(
        "Basic Constraints",
        "RFC5280 4.2.1.9",
    ),
    ExtensionOID.CERTIFICATE_POLICIES.dotted_string: OidInfo(
        "Certificate Policies", "RFC5280 4.2.1.4"
    ),
    ExtensionOID.CRL_DISTRIBUTION_POINTS.dotted_string: OidInfo(
        "CRL Distribution Points",
        "RFC5280 4.2.1.13",
    ),
    ExtensionOID.DELTA_CRL_INDICATOR.dotted_string: OidInfo(
        "Delta CRL INdicator",
        "RFC6962 5.2.4",
    ),
    ExtensionOID.EXTENDED_KEY_USAGE.dotted_string: OidInfo(
        "Extended Key Usage", "RFC5280 4.2.1.12"
    ),
    ExtensionOID.FRESHEST_CRL.dotted_string: OidInfo(
        "Freshest CRL", "RFC5280 4.2.1.15"
    ),
    ExtensionOID.ISSUER_ALTERNATIVE_NAME.dotted_string: OidInfo(
        "Issuer Alt Name", "RFC5280 4.2.1.7 and 5.2.2"
    ),
    ExtensionOID.KEY_USAGE.dotted_string: OidInfo("Key Usage", "RFC5280 4.2.1.3"),
    ExtensionOID.SIGNED_CERTIFICATE_TIMESTAMPS.dotted_string: OidInfo(
        "Signed Certificate Timestamp",
        None,
    ),
    ExtensionOID.SUBJECT_ALTERNATIVE_NAME.dotted_string: OidInfo(
        "Subject Alternative Name",
        "RFC5280 4.2.1.6",
    ),
    ExtensionOID.SUBJECT_KEY_IDENTIFIER.dotted_string: OidInfo(
        "Subject Key Identifier", "RFC5280 4.2.1.2"
    ),
    ExtensionOID.SUBJECT_INFORMATION_ACCESS.dotted_string: OidInfo(
        "Subject Information Access", "RFC5280 4.2.2.1"
    ),
    ExtensionOID.SUBJECT_DIRECTORY_ATTRIBUTES.dotted_string: OidInfo(
        "Subject Directory Attributes", "RFC5280 4.2.1.8"
    ),
    ExtensionOID.POLICY_CONSTRAINTS.dotted_string: OidInfo(
        "Policy Constraints", "RFC5280 4.2.1.11"
    ),
    ExtensionOID.POLICY_MAPPINGS.dotted_string: OidInfo(
        "Policy Mappings", "RFC5280 4.2.1.5"
    ),
    ExtensionOID.NAME_CONSTRAINTS.dotted_string: OidInfo(
        "Name Constraints", "RFC5280 4.2.1.10"
    ),
    ExtensionOID.CRL_NUMBER.dotted_string: OidInfo("CRL Number", "RFC6962 5.2.3"),
    ExtensionOID.ISSUING_DISTRIBUTION_POINT.dotted_string: OidInfo(
        "Issuing Distribution Point",
        "RFC6962 5.2.5",
    ),
    ExtensionOID.INHIBIT_ANY_POLICY.dotted_string: OidInfo(
        "Inhibit Any Policy",
        "RFC5280 4.2.1.14",
    ),
    ExtensionOID.PRECERT_SIGNED_CERTIFICATE_TIMESTAMPS.dotted_string: OidInfo(
        "CT Precertificate SCTs", "RFC6962 3.3"
    ),
    ExtensionOID.SIGNED_CERTIFICATE_TIMESTAMPS.dotted_string: OidInfo(
        "Certificate SCTs", "RFC6962 3.3"
    ),
    # Microsoft Extensions
    "1.3.6.1.4.1.311.21.7": OidInfo("Microsoft szOID_CERTIFICATE_TEMPLATE", None),
    "1.3.6.1.4.1.311.21.10": OidInfo("Microsoft szOID_APPLICATION_CERT_POLICIES", None),
    "1.3.6.1.4.1.311.13.2.3": OidInfo("szOID_OS_VERSION", None),
    "1.3.6.1.4.1.311.13.2.2": OidInfo("szOID_ENROLLMENT_CSP_PROVIDER", None),
    "1.3.6.1.4.1.311.2.1.14": OidInfo("Authenticode SPC_CERT_EXTENSIONS_OBJID", None),
    # Other extensions
    "1.2.840.113549.1.9.15": OidInfo("SMime Capabilities", "RFC8551"),
    "1.3.6.1.5.5.7.48.1.5": OidInfo("OCSP id-pkix-ocsp-nocheck extension", "RFC2560"),
    # endregion
    # region Signature Algorithm OIDs
    SignatureAlgorithmOID.DSA_WITH_SHA1.dotted_string: OidInfo(
        "DSA with SHA1", "FIPS Pub 186-4"
    ),
    SignatureAlgorithmOID.DSA_WITH_SHA224.dotted_string: OidInfo(
        "DSA with SHA224", "RFC5754"
    ),
    SignatureAlgorithmOID.DSA_WITH_SHA256.dotted_string: OidInfo(
        "DSA with SHA256", "RFC5754"
    ),
    SignatureAlgorithmOID.DSA_WITH_SHA384.dotted_string: OidInfo(
        "DSA with SHA384", "RFC5754"
    ),
    SignatureAlgorithmOID.DSA_WITH_SHA512.dotted_string: OidInfo(
        "DSA with SHA512", "RFC5754"
    ),
    SignatureAlgorithmOID.ECDSA_WITH_SHA1.dotted_string: OidInfo(
        "ECDSA with SHA1", "RFC5480"
    ),
    SignatureAlgorithmOID.ECDSA_WITH_SHA224.dotted_string: OidInfo(
        "ECDSA with SHA224", "RFC5480"
    ),
    SignatureAlgorithmOID.ECDSA_WITH_SHA256.dotted_string: OidInfo(
        "ECDSA with SHA256", "RFC5480"
    ),
    SignatureAlgorithmOID.ECDSA_WITH_SHA384.dotted_string: OidInfo(
        "ECDSA with SHA384", "RFC5480"
    ),
    SignatureAlgorithmOID.ECDSA_WITH_SHA512.dotted_string: OidInfo(
        "ECDSA with SHA512", "RFC5480"
    ),
    SignatureAlgorithmOID.RSA_WITH_SHA1.dotted_string: OidInfo(
        "RSA with SHA1", "RFC3174"
    ),
    SignatureAlgorithmOID.RSA_WITH_SHA224.dotted_string: OidInfo(
        "RSA with SHA224", "RFC8017"
    ),
    SignatureAlgorithmOID.RSA_WITH_SHA256.dotted_string: OidInfo(
        "RSA with SHA256", "RFC8017"
    ),
    SignatureAlgorithmOID.RSA_WITH_SHA384.dotted_string: OidInfo(
        "RSA with SHA384", "RFC8017"
    ),
    SignatureAlgorithmOID.RSA_WITH_SHA512.dotted_string: OidInfo(
        "RSA with SHA512", "RFC8017"
    ),
    SignatureAlgorithmOID.ED25519.dotted_string: OidInfo("ed-25519", None),
    SignatureAlgorithmOID.ED448.dotted_string: OidInfo(
        "Edwards-curve Digital Signature Algorithm (EdDSA) Ed448",
        "RFC8032",
    ),
    SignatureAlgorithmOID.GOSTR3410_2012_WITH_3411_2012_256.dotted_string: OidInfo(
        "GOST R 34.10-2012 with 34.11-2012 256", "RFC9215, RFC7091, RFC6986"
    ),
    SignatureAlgorithmOID.GOSTR3410_2012_WITH_3411_2012_512.dotted_string: OidInfo(
        "GOST R 34.10-2012 with 34.11-2012 512", "RFC9215, RFC7091, RFC6986"
    ),
    SignatureAlgorithmOID.GOSTR3411_94_WITH_3410_2001.dotted_string: OidInfo(
        "GOST R 34.11-94", "RFC4491"
    ),
    "1.2.156.10197.1.501": OidInfo("SM2 signature with SM3 hashing", None),
    "1.2.840.113549.1.1.10": OidInfo(
        "RSA Signature Scheme with Probabilistic Signature Scheme (RSASSA-PSS)",
        None,
    ),
    "1.2.840.113549.1.1.2": OidInfo("md2 With RSA Encryption", None),
    "1.2.840.113549.1.1.4": OidInfo("md5 With RSA Encryption", None),
    "1.2.840.113549.3.4": OidInfo("RSA with Rivest Cipher 4 (RC4)", None),
    # endregion
    # region Elliptic Curve OIDs
    EllipticCurveOID.BRAINPOOLP256R1.dotted_string: OidInfo(
        "brainpool256r1", "RFC5639"
    ),
    EllipticCurveOID.BRAINPOOLP384R1.dotted_string: OidInfo(
        "brainpool384r1", "RFC5639"
    ),
    EllipticCurveOID.BRAINPOOLP512R1.dotted_string: OidInfo(
        "brainpool512r1", "RFC5639"
    ),
    EllipticCurveOID.SECP192R1.dotted_string: OidInfo(
        "192-bit prime field Weierstrass curve (prime192v1, secp192r1, P-192)",
        "RFC5480",
    ),
    EllipticCurveOID.SECP224R1.dotted_string: OidInfo("secp224r1", "RFC5480"),
    EllipticCurveOID.SECP384R1.dotted_string: OidInfo("secp384r1", "RFC5480"),
    EllipticCurveOID.SECP521R1.dotted_string: OidInfo("secp512r1", "RFC5480"),
    EllipticCurveOID.SECT163K1.dotted_string: OidInfo("sect163k1", "RFC5480"),
    EllipticCurveOID.SECT163R2.dotted_string: OidInfo("sect163r2", "RFC5480"),
    EllipticCurveOID.SECT233K1.dotted_string: OidInfo("sect233k1", "RFC5480"),
    EllipticCurveOID.SECT233R1.dotted_string: OidInfo("sect233r1", "RFC5480"),
    EllipticCurveOID.SECT283K1.dotted_string: OidInfo("sect283k1", "RFC5480"),
    EllipticCurveOID.SECT283R1.dotted_string: OidInfo("sect283r1", "RFC5480"),
    EllipticCurveOID.SECT409K1.dotted_string: OidInfo("sect409k1", "RFC5480"),
    EllipticCurveOID.SECT409R1.dotted_string: OidInfo("sect409r1", "RFC5480"),
    EllipticCurveOID.SECT571K1.dotted_string: OidInfo("sect571k1", "RFC5480"),
    EllipticCurveOID.SECT571R1.dotted_string: OidInfo("sect571r1", "RFC5480"),
    "1.2.840.10045.3.1.2": OidInfo(
        "192-bit prime field Weierstrass curve (prime192v2)", "RFC3279"
    ),
    "1.2.840.10045.3.1.3": OidInfo(
        "192-bit prime field Weierstrass curve (prime192v3)", "RFC3279"
    ),
    "1.2.840.10045.3.1.4": OidInfo(
        "239-bit prime field Weierstrass curve (prime239v1)", "RFC3279"
    ),
    "1.2.840.10045.3.1.5": OidInfo(
        "239-bit prime field Weierstrass curve (prime239v2)", "RFC3279"
    ),
    "1.2.840.10045.3.1.6": OidInfo(
        "239-bit prime field Weierstrass curve (prime239v3)", "RFC3279"
    ),
    EllipticCurveOID.SECP256R1.dotted_string: OidInfo(
        "256-bit prime field Weierstrass curve (prime256v1, secp256r1, P-256)",
        "RFC5480",
    ),
    "1.2.840.10045.3.0.1": OidInfo("TwoCurve c2pnb163v1", "RFC3279"),
    "1.2.840.10045.3.0.2": OidInfo("TwoCurve c2pnb163v2", "RFC3279"),
    "1.2.840.10045.3.0.3": OidInfo("TwoCurve c2pnb163v3", "RFC3279"),
    "1.2.840.10045.3.0.4": OidInfo("TwoCurve c2pnb176w1", "RFC3279"),
    "1.2.840.10045.3.0.5": OidInfo("TwoCurve c2tnb191v1", "RFC3279"),
    "1.2.840.10045.3.0.6": OidInfo("TwoCurve c2tnb191v2", "RFC3279"),
    "1.2.840.10045.3.0.7": OidInfo("TwoCurve c2tnb191v3", "RFC3279"),
    "1.2.840.10045.3.0.8": OidInfo("TwoCurve c2tnb191v4", "RFC3279"),
    "1.2.840.10045.3.0.9": OidInfo("TwoCurve c2tnb191v5", "RFC3279"),
    "1.2.840.10045.3.0.10": OidInfo("TwoCurve c2pnb208w1", "RFC3279"),
    "1.2.840.10045.3.0.11": OidInfo("TwoCurve c2tnb239v1", "RFC3279"),
    "1.2.840.10045.3.0.12": OidInfo("TwoCurve c2tnb239v2", "RFC3279"),
    "1.2.840.10045.3.0.13": OidInfo("TwoCurve c2tnb239v3", "RFC3279"),
    "1.2.840.10045.3.0.14": OidInfo("TwoCurve c2onb239v4", "RFC3279"),
    "1.2.840.10045.3.0.15": OidInfo("TwoCurve c2onb239v5", "RFC3279"),
    "1.2.840.10045.3.0.16": OidInfo("TwoCurve c2pnb272w1", "RFC3279"),
    "1.2.840.10045.3.0.17": OidInfo("TwoCurve c2pnb304w1", "RFC3279"),
    "1.2.840.10045.3.0.18": OidInfo("TwoCurve c2tnb359v1", "RFC3279"),
    "1.2.840.10045.3.0.19": OidInfo("TwoCurve c2pnb368w1", "RFC3279"),
    "1.2.840.10045.3.0.20": OidInfo("TwoCurve c2tnb431r1", "RFC3279"),
    # endregion
    # region Certificate Policies
    "2.23.140.1.2.1": OidInfo(
        "CA/Browser Forum domain-validated",
        "https://cabforum.org/wp-content/uploads/CA-Browser-Forum-BR-1.8.4.pdf",
    ),
    "2.23.140.1.2.2": OidInfo(
        "CA/Browser Forum organization-validated",
        "https://cabforum.org/wp-content/uploads/CA-Browser-Forum-BR-1.8.4.pdf",
    ),
    "2.23.140.1.2.3": OidInfo(
        "CA/Browser Forum individual-validated",
        "https://cabforum.org/wp-content/uploads/CA-Browser-Forum-BR-1.8.4.pdf",
    ),
    "2.23.140.1.3": OidInfo(
        "CA/Browser Forum domain-extended-validation-codesigning",
        "https://cabforum.org/wp-content/uploads/Baseline-Requirements-for-the-Issuance-and-Management-of-Code-Signing.v3.0.pdf",
    ),
    "2.23.140.1.4.1": OidInfo(
        "CA/Browser Forum codesigning-requirements",
        "https://cabforum.org/wp-content/uploads/Baseline-Requirements-for-the-Issuance-and-Management-of-Code-Signing.v3.0.pdf",
    ),
    "2.23.140.1.31": OidInfo(
        "CA/Browser Forum onion-EV",
        "https://cabforum.org/wp-content/uploads/CA-Browser-Forum-EV-Guidelines-1.7.9.pdf",
    ),
    "2.23.140.3.1": OidInfo("CA/Browser Forum cabforganization-identifier", None),
    "1.3.6.1.4.1.11129.2.5.3": OidInfo(
        "Google Trust Services Certificate Policy",
        "https://pki.goog/GTS-CP-1.3.pdf",
    ),
    "1.3.6.1.4.1.311.76.509.1.1": OidInfo(
        "Microsoft PKI Services Certification Practice Statement (CPS)",
        "https://www.microsoft.com/pkiops/Docs/Content/policy/Microsoft_PKI_Services_CPS_v3.1.2.pdf",
    ),
    "1.3.6.1.4.1.6449.1.2.1.5.1": OidInfo(
        "Comodo Extended Validation (EV) Certification Practice Statement",
        "https://www.comodo.com/repository/EV_CPS_4_JUN_07.pdf",
    ),
    "1.3.6.1.4.1.4146.1.20": OidInfo(
        "GlobalSign Certificate Policy",
        "https://www.globalsign.com/en/repository",
    ),
    "2.16.840.1.114414.1.7.23.1": OidInfo(
        "Starfield Technologies Certificate Policy and Certification Practice Statement (CP/CPS)",
        "https://certs.starfieldtech.com/repository/certificate_practices/StarfieldCertificatePolicyandCertificationPracticeStatement.pdf",
    ),
    # endregion
    # region Hashes
    "1.2.840.113549.2.2": OidInfo("md2", None),
    "1.2.840.113549.2.5": OidInfo("md5", None),
    "1.3.14.3.2.26": OidInfo("id-sha1", None),
    "2.16.840.1.101.3.4.2.4": OidInfo("SHA224", "RFC3874"),
    # endregion
    "1.2.840.113549.3.7": OidInfo(
        "3DES in CBC mode (szOID_RSA_DES_EDE3_CBC)", "RFC8018"
    ),
    "1.3.14.3.2.7": OidInfo(
        "Single-key DES in CBC mode with padding operation", "RFC8018"
    ),
    "1.3.6.1.5.5.7.1.14": OidInfo("Proxy certification information", "RFC3820"),
    "1.2.840.113549.3.2": OidInfo("Voice encryption", "RFC8018"),
}
