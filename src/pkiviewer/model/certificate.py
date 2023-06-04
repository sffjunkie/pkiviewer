import datetime

import cryptography.exceptions
import cryptography.x509.name
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.x509 import Version
from cryptography.x509.base import Certificate

from pkiviewer.context import _config, _console  # type: ignore
from pkiviewer.model.common import get_extension_for_oid, sort_extensions_by_rfc_section
from pkiviewer.model.extension import v3_extension_parse
from pkiviewer.model.public_key import public_key_info
from pkiviewer.oid.names import Oid, OidNames
from pkiviewer.types import Error, PublicKeyInfo, Warning, X509ExtensionInfo, X509Info
from pkiviewer.view.console import print_info


def verbose() -> bool:
    c = _config.get()
    return c["output"].get("verbose", False)


class CertificateInfo(X509Info):
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
    fingerprint: bytes


def certiticate_parse(cert: Certificate, filename: str):
    errors: list[Error] = []
    warnings: list[Warning] = []

    try:
        pk = cert.public_key()
        pk_info = public_key_info(pk)
    except (cryptography.exceptions.UnsupportedAlgorithm, ValueError) as exc:
        pk_info = None
        errors.append(
            Error(
                module="cryptography",
                text=f"Public key decode; {exc}",
            )
        )

    extensions = {}
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
                    warnings.append(
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

                        extensions[oid] = extension_info
                except KeyError:
                    if oid in OidNames:
                        name = f"{OidNames[oid].name} (OID:{oid})"
                    else:
                        name = f"OID:{oid}"
                    warnings.append(
                        Warning(
                            module="pkiviewer",
                            text=f"Parse function for X.509 extension {name} not found",
                        )
                    )
        except ValueError as exc:
            print(exc)
            _console.get().print_exception()

    info: CertificateInfo = {
        "type": "certificate",
        "filename": filename,
        "version": cert.version,
        "serial_number": cert.serial_number,
        "signature": cert.signature,
        "signature_algorithm_oid": cert.signature_algorithm_oid.dotted_string,
        "issuer": cert.issuer,
        "not_valid_before": cert.not_valid_before,
        "not_valid_after": cert.not_valid_after,
        "subject": cert.subject,
        "public_key": pk_info,
        "extensions": extensions,
        "errors": errors,
        "warnings": warnings,
        "fingerprint": cert.fingerprint(SHA256()),
    }

    return info
