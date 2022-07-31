from typing import Any

from pkiviewer.asn1.load_specification import load_asn1_specification  # type: ignore


def decode_crl(data: bytes) -> dict[Any, Any] | None:
    crl_asn1 = load_asn1_specification("tbs_certlist.asn1")  # type: ignore
    if crl_asn1 is not None:
        info: dict[Any, Any] = crl_asn1.decode("TBSCertList", data)  # type: ignore
        return info

    return None
