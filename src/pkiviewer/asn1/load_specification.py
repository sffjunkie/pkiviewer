from pathlib import Path

import asn1tools  # type: ignore


def load_asn1_specification(spec_name: str) -> asn1tools.compiler.Specification | None:  # type: ignore
    p = Path(__file__).parent / "specs" / spec_name
    q = str(p.resolve())
    crl_asn1: asn1tools.compiler.Specification | None = asn1tools.compile_files(  # type: ignore
        q, codec="der"
    )
    return crl_asn1  # type: ignore
