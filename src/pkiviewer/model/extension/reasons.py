from cryptography.x509 import ReasonFlags


Reasons: dict[ReasonFlags, str] = {
    ReasonFlags.aa_compromise: "Attribute Authority compromised",
    ReasonFlags.affiliation_changed: "Subject's name or other information has changed",
    ReasonFlags.ca_compromise: "Certificate Authority compromised",
    ReasonFlags.certificate_hold: "Certificate on hold",
    ReasonFlags.cessation_of_operation: "Certificate no longer required",
    ReasonFlags.key_compromise: "Private key was compromised",
    ReasonFlags.privilege_withdrawn: "Privilege granted by this certificate have been withdrawn",
    ReasonFlags.remove_from_crl: "Certificate should be removed from the CRL",
    ReasonFlags.superseded: "Certificate superseded",
    ReasonFlags.unspecified: "Unspecified",
}


def reasons_parse(reasons: frozenset[ReasonFlags] | None) -> list[str]:
    if reasons is None:
        return []
    return [Reasons[flag] for flag in reasons]
