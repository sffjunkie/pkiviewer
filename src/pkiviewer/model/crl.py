import datetime
from zoneinfo import ZoneInfo
from typing import TypedDict

from cryptography.x509 import CertificateRevocationList
from cryptography.hazmat.primitives import hashes

import cryptography.x509.name
import cryptography.exceptions
from asn1tools.codecs import generalized_time_to_datetime  # type: ignore

from pkiviewer.model import X509ExtensionInfo
from pkiviewer.types import Warning, Error
from pkiviewer.oid import Oid, OidNames
from pkiviewer.model.extension import v3_extension_parse
from pkiviewer.context import _console  # type: ignore

from pkiviewer.asn1 import decode_tbs_certlist

CertificateID = int

X509RevocationDate = tuple[str, datetime.datetime]


class X509RevocationInfo(TypedDict):
    userCertificate: CertificateID
    revocationDate: X509RevocationDate


RevokedAt = datetime.datetime


class RevocationInfo(TypedDict):
    certificate_id: CertificateID
    revocation_date: RevokedAt


class CertificateRevocationListInfo(TypedDict):
    filename: str
    signature: bytes | None
    signature_algorithm: str
    signature_algorithm_oid: str
    signature_hash_algorithm: hashes.HashAlgorithm | None
    issuer: cryptography.x509.name.Name
    last_update: datetime.datetime | None
    next_update: datetime.datetime | None
    errors: list[Error]
    warnings: list[Warning]
    fingerprint: bytes | None
    extensions: dict[Oid, X509ExtensionInfo]
    revoked_certificates: list[RevocationInfo]
    errors: list[Error]
    warnings: list[Warning]
    fingerprint: bytes | None


def revocation_date_parse(x509_dt: X509RevocationDate) -> datetime.datetime:
    if x509_dt[0] == "utcTime":
        return x509_dt[1].replace(tzinfo=ZoneInfo("UTC"))
    else:
        return x509_dt[1]


def revocation_info_parse(
    revocation_info: list[X509RevocationInfo],
) -> list[RevocationInfo]:
    info: list[RevocationInfo] = []
    for item in revocation_info:
        dt = item["revocationDate"]
        rinfo: RevocationInfo = {
            "certificate_id": item["userCertificate"],
            "revocation_date": revocation_date_parse(dt),
        }
        info.append(rinfo)
    return info


def certiticate_revocation_list_parse(crl: CertificateRevocationList, filename: str):
    rl = decode_tbs_certlist.decode_crl(crl.tbs_certlist_bytes)  # type: ignore
    revoked_certificates = revocation_info_parse(rl["revokedCertificates"])  # type: ignore

    if crl.signature_hash_algorithm:
        fingerprint = crl.fingerprint(crl.signature_hash_algorithm)
    else:
        fingerprint = None

    extensions = {}
    errors: list[Error] = []
    warnings: list[Warning] = []
    try:
        for extension in crl.extensions:
            oid = extension.oid.dotted_string
            try:
                name = OidNames[oid].name
            except KeyError:
                warnings.append(
                    Warning(
                        module="pkiviewer",
                        text=f"Unknown extension name for oid {oid}",
                    )
                )
                continue

            try:
                func = v3_extension_parse[oid]
                if func is not None:
                    extension_info: X509ExtensionInfo = {
                        "oid": oid,
                        "name": name,
                        "critical": extension.critical,
                        "info": func(extension.value),
                    }
                    extensions[oid] = extension_info
            except KeyError:
                if oid in OidNames:
                    name = f"{OidNames[oid]} (OID:{oid})"
                else:
                    name = f"OID:{oid}"
                warnings.append(
                    Warning(
                        module="pkiviewer",
                        text=f"Parse function for X.509 extension {name} not found",
                    )
                )
    except ValueError as exc:
        errors.append(Error(module="pkiviewer", text=exc.args[0]))

    info: CertificateRevocationListInfo = {
        "filename": filename,
        "signature": crl.signature,
        "signature_algorithm": OidNames[crl.signature_algorithm_oid.dotted_string].name,
        "signature_algorithm_oid": crl.signature_algorithm_oid.dotted_string,
        "signature_hash_algorithm": crl.signature_hash_algorithm,
        "issuer": crl.issuer,
        "last_update": crl.last_update,
        "next_update": crl.next_update,
        "errors": errors,
        "warnings": warnings,
        "extensions": extensions,
        "fingerprint": fingerprint,
        "revoked_certificates": revoked_certificates,
    }

    return info
