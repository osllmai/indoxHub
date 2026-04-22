"""Uploads: multipart pass-through to Resemble's storage."""

from typing import Any, Dict

from ._base import _ResembleResource


class _Uploads(_ResembleResource):
    _prefix = "/resemble/uploads"

    def create(self, file_path: str) -> Dict[str, Any]:
        """Upload a local file and receive back Resemble's storage URL.

        The returned URL can be passed as audio_url/video_url to STT,
        enhance, edit, detect, intelligence, watermark, identity endpoints.
        """
        with open(file_path, "rb") as f:
            files = {"file": f}
            return self._request("POST", "", data=None, files=files)
