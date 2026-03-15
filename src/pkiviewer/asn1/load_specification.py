# from pathlib import Path

import pyasn1  # type: ignore

pyasn1 = pyasn1


def load_asn1_specification(
    spec_name: str,
) -> str | None:
    # ) -> asn1tools.compiler.Specification | None:  # type: ignore
    # p = Path(__file__).parent / "specs" / spec_name
    # q = str(p.resolve())
    # crl_asn1: asn1tools.compiler.Specification | None = asn1tools.compile_files(
    #     q, codec="der"
    # )  # type: ignore
    # return crl_asn1  # type: ignore
    return None


def load_future_asn1_specifications(specs: list[str]):
    # p = Path(__file__).parent / "specs" / "future"

    # sf = [str((p / f).resolve()) for f in specs]
    # specs = asn1tools.compile_files(sf)
    specs = []
    return specs
