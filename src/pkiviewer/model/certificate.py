import datetime
from typing import TypedDict

import cryptography.x509.name
import cryptography.exceptions

from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.x509 import Version
from cryptography.x509.base import Certificate

from pkiviewer.types import Warning, Error
from pkiviewer.model import PublicKeyInfo, X509ExtensionInfo
from pkiviewer.model.public_key import public_key_info
from pkiviewer.model.common import sort_extensions_by_rfc_section, get_extension_for_oid
from pkiviewer.model.extension import v3_extension_parse
from pkiviewer.oid import Oid, OidNames
from pkiviewer.view.console import print_info
from pkiviewer.context import _console, _config  # type: ignore


def verbose() -> bool:
    c = _config.get()
    return c["output"].get("verbose", False)


class CertificateInfo(TypedDict, total=False):
    filename: str
    version: Version
    serial_number: int
    signature: bytes
    signature_algorithm_oid: str
    issuer: cryptography.x509.name.Name
    not_valid_before: datetime.datetime
    not_valid_after: datetime.datetime
    subject: cryptography.x509.name.Name
    public_key: PublicKeyInfo | None
    extensions: dict[Oid, X509ExtensionInfo]
    errors: list[Error]
    warnings: list[Warning]
    fingerprint: bytes


def certiticate_parse(cert: Certificate, filename: str):
    info: CertificateInfo = {
        "filename": filename,
        "version": cert.version,
        "serial_number": cert.serial_number,
        "signature": cert.signature,
        "signature_algorithm_oid": cert.signature_algorithm_oid.dotted_string,
        "issuer": cert.issuer,
        "not_valid_before": cert.not_valid_before,
        "not_valid_after": cert.not_valid_after,
        "subject": cert.subject,
        "extensions": {},
        "errors": [],
        "warnings": [],
        "fingerprint": cert.fingerprint(SHA256()),
    }

    try:
        pk = cert.public_key()
        info["public_key"] = public_key_info(pk)
    except (cryptography.exceptions.UnsupportedAlgorithm, ValueError) as exc:
        info["public_key"] = None
        info["errors"].append(
            Error(
                module="cryptography",
                text=f"Public key decode; {exc}",
            )
        )

    if cert.version == Version.v3:
        try:
            se = sort_extensions_by_rfc_section(cert.extensions)
            for item in se:
                oid = item[2]
                extension = get_extension_for_oid(cert.extensions, oid)
                if extension is None:
                    continue

                try:
                    name = OidNames[oid].name
                except KeyError:
                    info["warnings"].append(
                        Warning(
                            module="pkiviewer",
                            text=f"Unknown extension name for oid {oid}, skipping",
                        )
                    )
                    continue

                try:
                    func = v3_extension_parse[oid]
                    if func is not None:
                        if verbose():
                            print_info(f"Parsing extension {name} (oid:{oid})")

                        extension_info: X509ExtensionInfo = {
                            "oid": oid,
                            "name": name,
                            "critical": extension.critical,
                            "info": func(extension.value),
                        }

                        info["extensions"][oid] = extension_info
                except KeyError as exc:
                    if oid in OidNames:
                        name = f"{OidNames[oid].name} (OID:{oid})"
                    else:
                        name = f"OID:{oid}"
                    info["warnings"].append(
                        Warning(
                            module="pkiviewer",
                            text=f"Parse function for X.509 extension {name} not found",
                        )
                    )
        except ValueError as exc:
            print(exc)
            _console.get().print_exception()

    return info
