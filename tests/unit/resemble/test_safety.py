"""Unit tests for client.resemble.safety.*"""

import pytest


@pytest.mark.unit
@pytest.mark.parametrize(
    "capability,expected_path",
    [
        ("detect", "resemble/detect"),
        ("intelligence", "resemble/intelligence"),
        ("tracing", "resemble/tracing"),
    ],
)
def test_submit(mock_client, capability, expected_path):
    getattr(mock_client.resemble.safety, capability)(audio_url="https://x.mp3")
    args = mock_client._request.call_args[0]
    assert args[0] == "POST"
    assert args[1] == expected_path
    assert args[2] == {"audio_url": "https://x.mp3"}


@pytest.mark.unit
@pytest.mark.parametrize(
    "getter,expected_path",
    [
        ("get_detect", "resemble/detect/job-1"),
        ("get_intelligence", "resemble/intelligence/job-1"),
        ("get_tracing", "resemble/tracing/job-1"),
    ],
)
def test_get(mock_client, getter, expected_path):
    getattr(mock_client.resemble.safety, getter)("job-1")
    args = mock_client._request.call_args[0]
    assert args[0] == "GET"
    assert args[1] == expected_path


@pytest.mark.unit
def test_submit_strips_none(mock_client):
    mock_client.resemble.safety.detect(audio_url="x", modality=None, foo="bar")
    _, _, data = mock_client._request.call_args[0]
    assert "modality" not in data
    assert data == {"audio_url": "x", "foo": "bar"}
