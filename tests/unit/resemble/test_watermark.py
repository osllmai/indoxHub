"""Unit tests for client.resemble.watermark.*"""

import pytest


@pytest.mark.unit
def test_apply(mock_client):
    mock_client.resemble.watermark.apply(audio_url="https://x.mp3", payload="abc")
    args = mock_client._request.call_args[0]
    assert args[0] == "POST"
    assert args[1] == "resemble/watermark/apply"
    assert args[2] == {"audio_url": "https://x.mp3", "payload": "abc"}


@pytest.mark.unit
def test_get_apply(mock_client):
    mock_client.resemble.watermark.get_apply("job-1")
    assert mock_client._request.call_args[0][:2] == ("GET", "resemble/watermark/apply/job-1")


@pytest.mark.unit
def test_detect(mock_client):
    mock_client.resemble.watermark.detect(audio_url="https://x.mp3")
    args = mock_client._request.call_args[0]
    assert args[0] == "POST"
    assert args[1] == "resemble/watermark/detect"


@pytest.mark.unit
def test_get_detect(mock_client):
    mock_client.resemble.watermark.get_detect("job-1")
    assert mock_client._request.call_args[0][:2] == ("GET", "resemble/watermark/detect/job-1")
