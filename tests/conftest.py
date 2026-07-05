"""Test configuration for Backup Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "backup-agent", "category": "Cloud Engineering"}
