"""Unit tests for client.resemble.voice_design.*"""

import pytest


@pytest.mark.unit
def test_generate_candidates_minimal(mock_client):
    mock_client.resemble.voice_design.generate_candidates(description="warm baritone")
    args = mock_client._request.call_args[0]
    assert args[0] == "POST"
    assert args[1] == "resemble/voice-design/candidates"
    assert args[2] == {"description": "warm baritone"}


@pytest.mark.unit
def test_generate_candidates_full(mock_client):
    mock_client.resemble.voice_design.generate_candidates(
        description="warm baritone",
        sample_text="Hello there",
        params={"gender": "male"},
    )
    _, _, data = mock_client._request.call_args[0]
    assert data == {
        "description": "warm baritone",
        "sample_text": "Hello there",
        "params": {"gender": "male"},
    }


@pytest.mark.unit
def test_promote(mock_client):
    mock_client.resemble.voice_design.promote(
        design_uuid="d-1", candidate_index=2, name="MyNewVoice"
    )
    args = mock_client._request.call_args[0]
    assert args[0] == "POST"
    assert args[1] == "resemble/voice-design/d-1/promote"
    assert args[2] == {"candidate_index": 2, "name": "MyNewVoice"}
