"""Unit tests for client.resemble.stt.*"""

import pytest


@pytest.mark.unit
def test_create_minimal(mock_client):
    mock_client.resemble.stt.create(audio_url="https://x.mp3")
    args = mock_client._request.call_args[0]
    assert args[0] == "POST"
    assert args[1] == "resemble/stt"
    assert args[2] == {"audio_url": "https://x.mp3"}


@pytest.mark.unit
def test_create_full(mock_client):
    mock_client.resemble.stt.create(
        audio_url="https://x.mp3", language="en", callback_uri="https://cb"
    )
    _, _, data = mock_client._request.call_args[0]
    assert data == {
        "audio_url": "https://x.mp3",
        "language": "en",
        "callback_uri": "https://cb",
    }


@pytest.mark.unit
def test_get(mock_client):
    mock_client.resemble.stt.get("job-1")
    args = mock_client._request.call_args[0]
    assert args[0] == "GET"
    assert args[1] == "resemble/stt/job-1"


@pytest.mark.unit
def test_list(mock_client):
    mock_client.resemble.stt.list(page=2, page_size=50)
    args = mock_client._request.call_args[0]
    assert args[0] == "GET"
    assert args[1] == "resemble/stt?page=2&page_size=50"
