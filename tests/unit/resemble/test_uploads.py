"""Unit tests for client.resemble.uploads.create()"""

import os
import tempfile

import pytest


@pytest.mark.unit
def test_create(mock_client):
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        f.write(b"fake audio bytes")
        tmp_path = f.name
    try:
        mock_client.resemble.uploads.create(tmp_path)
        args, kwargs = mock_client._request.call_args
        assert args[0] == "POST"
        assert args[1] == "resemble/uploads"
        # data is None, files dict carries the upload
        assert args[2] is None
        assert "files" in kwargs
        assert "file" in kwargs["files"]
    finally:
        os.unlink(tmp_path)
