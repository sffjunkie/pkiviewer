import pytest

from pkiviewer.config import Configuration, config_load
from pkiviewer.context import _config  # type: ignore


@pytest.fixture(scope="module")
def config() -> Configuration:
    config_load()
    return _config.get()
