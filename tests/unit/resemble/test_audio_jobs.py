"""Unit tests for client.resemble.audio_jobs.*"""

import pytest


@pytest.mark.unit
def test_enhance(mock_client):
    mock_client.resemble.audio_jobs.enhance(audio_url="https://x.mp3")
    args = mock_client._request.call_args[0]
    assert args[0] == "POST"
    assert args[1] == "resemble/enhance"
    assert args[2] == {"audio_url": "https://x.mp3"}


@pytest.mark.unit
def test_enhance_with_fields(mock_client):
    mock_client.resemble.audio_jobs.enhance(
        audio_url="https://x.mp3", denoise_level=0.7
    )
    _, _, data = mock_client._request.call_args[0]
    assert data["denoise_level"] == 0.7


@pytest.mark.unit
def test_get_enhance(mock_client):
    mock_client.resemble.audio_jobs.get_enhance("job-1")
    args = mock_client._request.call_args[0]
    assert args[0] == "GET"
    assert args[1] == "resemble/enhance/job-1"


@pytest.mark.unit
def test_edit(mock_client):
    mock_client.resemble.audio_jobs.edit(
        audio_url="https://x.mp3",
        operations=[{"type": "remove", "start": 1, "end": 2}],
    )
    args = mock_client._request.call_args[0]
    assert args[0] == "POST"
    assert args[1] == "resemble/edit"
    assert args[2]["audio_url"] == "https://x.mp3"
    assert args[2]["operations"]


@pytest.mark.unit
def test_get_edit(mock_client):
    mock_client.resemble.audio_jobs.get_edit("job-1")
    args = mock_client._request.call_args[0]
    assert args[0] == "GET"
    assert args[1] == "resemble/edit/job-1"
