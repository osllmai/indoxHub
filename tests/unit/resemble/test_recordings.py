"""Unit tests for client.resemble.recordings.*"""

import pytest


@pytest.mark.unit
def test_list(mock_client):
    mock_client.resemble.recordings.list("v-1")
    args = mock_client._request.call_args[0]
    assert args[0] == "GET"
    assert args[1] == "resemble/voices/v-1/recordings?page=1&page_size=10"


@pytest.mark.unit
def test_list_with_pagination(mock_client):
    mock_client.resemble.recordings.list("v-1", page=2, page_size=25)
    assert (
        mock_client._request.call_args[0][1]
        == "resemble/voices/v-1/recordings?page=2&page_size=25"
    )


@pytest.mark.unit
def test_create(mock_client):
    mock_client.resemble.recordings.create("v-1", {"audio_url": "https://x.mp3"})
    args = mock_client._request.call_args[0]
    assert args[0] == "POST"
    assert args[1] == "resemble/voices/v-1/recordings"
    assert args[2] == {"fields": {"audio_url": "https://x.mp3"}}


@pytest.mark.unit
def test_get(mock_client):
    mock_client.resemble.recordings.get("v-1", "r-1")
    args = mock_client._request.call_args[0]
    assert args[0] == "GET"
    assert args[1] == "resemble/voices/v-1/recordings/r-1"


@pytest.mark.unit
def test_update(mock_client):
    mock_client.resemble.recordings.update("v-1", "r-1", {"name": "new"})
    args = mock_client._request.call_args[0]
    assert args[0] == "PUT"
    assert args[1] == "resemble/voices/v-1/recordings/r-1"
    assert args[2] == {"fields": {"name": "new"}}


@pytest.mark.unit
def test_delete(mock_client):
    mock_client.resemble.recordings.delete("v-1", "r-1")
    args = mock_client._request.call_args[0]
    assert args[0] == "DELETE"
    assert args[1] == "resemble/voices/v-1/recordings/r-1"
