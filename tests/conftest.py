"""Configuration for pytest."""
import os

import pandas as pd
import pytest
from _pytest.config import Config
from pandera.typing import DataFrame

from socceraction.atomic.spadl import AtomicSPADLSchema
from socceraction.spadl import SPADLSchema


def pytest_configure(config: Config) -> None:
    """Pytest configuration hook."""
    config.addinivalue_line("markers", "e2e: mark as end-to-end test.")


@pytest.fixture(scope='session')
def spadl_actions() -> DataFrame[SPADLSchema]:
    json_file = os.path.join(os.path.dirname(__file__), 'datasets', 'spadl', 'spadl.json')
    return pd.read_json(json_file, orient='records')


@pytest.fixture(scope='session')
def atomic_spadl_actions() -> DataFrame[AtomicSPADLSchema]:
    json_file = os.path.join(os.path.dirname(__file__), 'datasets', 'spadl', 'atomic_spadl.json')
    return pd.read_json(json_file, orient='records')
