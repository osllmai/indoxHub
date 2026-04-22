"""Audio enhance + audio edit (async submit/retrieve)."""

from typing import Any, Dict

from ._base import _ResembleResource


class _AudioJobs(_ResembleResource):
    """Wrapper over two sibling capabilities: enhance and edit.

    Paths are /resemble/enhance and /resemble/edit respectively — we override
    the prefix per call rather than using _prefix directly.
    """

    _prefix = "/resemble"

    def enhance(self, audio_url: str, **fields: Any) -> Dict[str, Any]:
        """Submit an audio-enhancement job. Bills audio_seconds."""
        data = {"audio_url": audio_url, **{k: v for k, v in fields.items() if v is not None}}
        return self._request("POST", "/enhance", data)

    def get_enhance(self, job_id: str) -> Dict[str, Any]:
        """Retrieve enhancement result."""
        return self._request("GET", f"/enhance/{job_id}")

    def edit(self, audio_url: str, **fields: Any) -> Dict[str, Any]:
        """Submit an audio-edit job. Bills audio_seconds."""
        data = {"audio_url": audio_url, **{k: v for k, v in fields.items() if v is not None}}
        return self._request("POST", "/edit", data)

    def get_edit(self, job_id: str) -> Dict[str, Any]:
        """Retrieve edit result."""
        return self._request("GET", f"/edit/{job_id}")
