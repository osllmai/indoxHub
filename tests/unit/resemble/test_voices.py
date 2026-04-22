"""Unit tests for client.resemble.voices.*"""

import pytest


@pytest.mark.unit
def test_create_minimal(mock_client):
    mock_client.resemble.voices.create(name="MyVoice")
    args = mock_client._request.call_args[0]
    assert args[0] == "POST"
    assert args[1] == "resemble/voices"
    assert args[2] == {"name": "MyVoice"}


@pytest.mark.unit
def test_create_with_optionals(mock_client):
    mock_client.resemble.voices.create(
        name="MyVoice",
        consent_text="I consent...",
        description="A warm voice",
    )
    _, _, data = mock_client._request.call_args[0]
    assert data == {
        "name": "MyVoice",
        "consent_text": "I consent...",
        "description": "A warm voice",
    }


@pytest.mark.unit
def test_build(mock_client):
    mock_client.resemble.voices.build("v-1", recording_ids=["r-1", "r-2"])
    args = mock_client._request.call_args[0]
    assert args[0] == "POST"
    assert args[1] == "resemble/voices/v-1/build"
    assert args[2] == {"recording_ids": ["r-1", "r-2"]}


@pytest.mark.unit
def test_delete(mock_client):
    mock_client.resemble.voices.delete("v-1")
    args = mock_client._request.call_args[0]
    assert args[0] == "DELETE"
    assert args[1] == "resemble/voices/v-1"
