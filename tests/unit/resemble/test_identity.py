"""Unit tests for client.resemble.identity.*"""

import pytest


@pytest.mark.unit
def test_search(mock_client):
    mock_client.resemble.identity.search(audio_url="https://x.mp3")
    args = mock_client._request.call_args[0]
    assert args[0] == "POST"
    assert args[1] == "resemble/identity/search"
    assert args[2] == {"audio_url": "https://x.mp3"}


@pytest.mark.unit
def test_enroll(mock_client):
    mock_client.resemble.identity.enroll(audio_url="https://x.mp3", name="Alice")
    args = mock_client._request.call_args[0]
    assert args[0] == "POST"
    assert args[1] == "resemble/identity/enroll"
    assert args[2] == {"audio_url": "https://x.mp3", "name": "Alice"}


@pytest.mark.unit
def test_list(mock_client):
    mock_client.resemble.identity.list(page=3, page_size=25)
    args = mock_client._request.call_args[0]
    assert args[0] == "GET"
    assert args[1] == "resemble/identity?page=3&page_size=25"


@pytest.mark.unit
def test_get(mock_client):
    mock_client.resemble.identity.get("id-1")
    assert mock_client._request.call_args[0][:2] == ("GET", "resemble/identity/id-1")


@pytest.mark.unit
def test_delete(mock_client):
    mock_client.resemble.identity.delete("id-1")
    assert mock_client._request.call_args[0][:2] == ("DELETE", "resemble/identity/id-1")
