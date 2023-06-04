import importlib.resources
import string
from enum import Enum, auto
from typing import NamedTuple


class Stage(Enum):
    INIT = auto()
    IN_RECORD = auto()


PenID = int


class PrivateEnterpriseNumber(NamedTuple):
    id: PenID
    organization: str
    contact: str
    email: str

    @property
    def oid(self) -> str:
        return f"1.3.6.1.4.1.{self.id}"


PrivateEnterpriseDatabase = dict[PenID, PrivateEnterpriseNumber]


def load_numbers() -> PrivateEnterpriseDatabase:
    pen_file = importlib.resources.files(__package__) / "enterprise-numbers.txt"
    db = PrivateEnterpriseDatabase()
    id_ = -1
    organization = ""
    contact = ""
    email = ""
    with pen_file.open() as penfp:
        for line in penfp:
            if line[0] in string.digits:
                if id_ != -1:
                    db[id_] = PrivateEnterpriseNumber(id_, organization, contact, email)
                id_ = int(line.strip())
            elif line.startswith("      "):
                email = line.strip()
            elif line.startswith("    "):
                contact = line.strip()
            elif line.startswith("  "):
                organization = line.strip()

    return db
