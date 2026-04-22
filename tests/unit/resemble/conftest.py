"""Shared fixtures for Resemble sub-module unit tests."""

from unittest.mock import MagicMock, patch

import pytest

from indoxhub import Client


@pytest.fixture
def mock_client():
    """Return a Client whose _authenticate is a no-op and whose _request is a
    MagicMock. Tests assert on (method, endpoint, data) triples and return
    canned payloads from the mock.
    """
    with patch.object(Client, "_authenticate", return_value=None):
        client = Client(api_key="test_api_key")
        client._request = MagicMock(return_value={"ok": True})
        try:
            yield client
        finally:
            client.close()
