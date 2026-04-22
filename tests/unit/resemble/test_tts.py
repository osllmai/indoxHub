"""Unit tests for client.resemble.tts.*"""

import pytest


@pytest.mark.unit
def test_synthesize_minimal(mock_client):
    mock_client._request.return_value = {
        "request_id": "res_abc",
        "audio_content": "b64data",
        "audio_duration": 1.42,
    }
    result = mock_client.resemble.tts.synthesize(voice_uuid="v-1", text="Hi")

    mock_client._request.assert_called_once()
    args, _ = mock_client._request.call_args
    method, endpoint, data = args[0], args[1], args[2]
    assert method == "POST"
    assert endpoint == "resemble/tts/synthesize"
    assert data == {"voice_uuid": "v-1", "text": "Hi", "output_format": "mp3"}
    assert result["request_id"] == "res_abc"


@pytest.mark.unit
def test_synthesize_with_optionals(mock_client):
    mock_client.resemble.tts.synthesize(
        voice_uuid="v-1",
        text="Hi",
        output_format="wav",
        precision="PCM_16",
        sample_rate=24000,
        language="en",
        speed=1.2,
    )
    _, _, data = mock_client._request.call_args[0]
    assert data["output_format"] == "wav"
    assert data["precision"] == "PCM_16"
    assert data["sample_rate"] == 24000
    assert data["language"] == "en"
    assert data["speed"] == 1.2


@pytest.mark.unit
def test_synthesize_skips_none_fields(mock_client):
    mock_client.resemble.tts.synthesize(voice_uuid="v-1", text="Hi")
    _, _, data = mock_client._request.call_args[0]
    # Only required fields + default output_format
    assert set(data.keys()) == {"voice_uuid", "text", "output_format"}


@pytest.mark.unit
def test_list_voices_defaults(mock_client):
    mock_client.resemble.tts.list_voices()
    args = mock_client._request.call_args[0]
    assert args[0] == "GET"
    assert args[1] == "resemble/tts/voices?page=1&page_size=10"


@pytest.mark.unit
def test_list_voices_pagination(mock_client):
    mock_client.resemble.tts.list_voices(page=3, page_size=50)
    args = mock_client._request.call_args[0]
    assert args[1] == "resemble/tts/voices?page=3&page_size=50"


@pytest.mark.unit
def test_get_voice(mock_client):
    mock_client.resemble.tts.get_voice("9fd7430d")
    args = mock_client._request.call_args[0]
    assert args[0] == "GET"
    assert args[1] == "resemble/tts/voices/9fd7430d"
