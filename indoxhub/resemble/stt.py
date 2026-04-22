"""Speech-to-Text (async jobs)."""

from typing import Any, Dict, Optional

from ._base import _ResembleResource


class _STT(_ResembleResource):
    _prefix = "/resemble/stt"

    def create(
        self,
        audio_url: str,
        language: Optional[str] = None,
        callback_uri: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Submit a transcription job. Returns a job_id — poll with get()."""
        data: Dict[str, Any] = {"audio_url": audio_url}
        if language is not None:
            data["language"] = language
        if callback_uri is not None:
            data["callback_uri"] = callback_uri
        return self._request("POST", "", data)

    def get(self, job_id: str) -> Dict[str, Any]:
        """Fetch transcript / job status."""
        return self._request("GET", f"/{job_id}")

    def list(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """List transcription jobs."""
        return self._request("GET", f"?page={page}&page_size={page_size}")
