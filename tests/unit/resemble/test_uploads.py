"""Unit tests for client.resemble.uploads.create()"""

import os
import tempfile

import pytest


@pytest.mark.unit
def test_create_no_purpose(mock_client):
    """Default behavior: no purpose -> data=None, server picks 'uploads/' prefix."""
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        f.write(b"fake audio bytes")
        tmp_path = f.name
    try:
        mock_client.resemble.uploads.create(tmp_path)
        args, kwargs = mock_client._request.call_args
        assert args[0] == "POST"
        assert args[1] == "resemble/uploads"
        assert args[2] is None
        assert "files" in kwargs
        assert "file" in kwargs["files"]
    finally:
        os.unlink(tmp_path)


@pytest.mark.unit
def test_create_with_voice_clone_purpose(mock_client):
    """purpose=voice_clone -> data={'purpose': 'voice_clone'} for permanent retention."""
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        f.write(b"fake voice clone source")
        tmp_path = f.name
    try:
        mock_client.resemble.uploads.create(tmp_path, purpose="voice_clone")
        args, kwargs = mock_client._request.call_args
        assert args[0] == "POST"
        assert args[1] == "resemble/uploads"
        assert args[2] == {"purpose": "voice_clone"}
        assert "files" in kwargs and "file" in kwargs["files"]
    finally:
        os.unlink(tmp_path)


@pytest.mark.unit
@pytest.mark.parametrize(
    "purpose", ["voice_clone", "stt_input", "watermark_input", "audio_job_input"]
)
def test_create_all_purposes_pass_through(mock_client, purpose):
    """Every documented purpose value is forwarded as a form field."""
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        f.write(b"x")
        tmp_path = f.name
    try:
        mock_client.resemble.uploads.create(tmp_path, purpose=purpose)
        args, _ = mock_client._request.call_args
        assert args[2] == {"purpose": purpose}
    finally:
        os.unlink(tmp_path)


@pytest.mark.unit
def test_create_explicit_none_purpose(mock_client):
    """purpose=None (explicitly) behaves like default — no form data."""
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        f.write(b"x")
        tmp_path = f.name
    try:
        mock_client.resemble.uploads.create(tmp_path, purpose=None)
        args, _ = mock_client._request.call_args
        assert args[2] is None
    finally:
        os.unlink(tmp_path)
