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
        """Retrieve enhancement result.

        Once the job is completed, the response is augmented with:
          - ``audio_url``: presigned Cloudflare R2 URL to the enhanced audio
            (7-day retention).
          - ``expires_at``: ISO 8601 timestamp when the R2 object expires.
          - ``resemble_url``: original upstream URL (kept as fallback).

        Mirroring is lazy + idempotent — first GET after completion writes
        to R2, subsequent GETs return the same R2 URL.
        """
        return self._request("GET", f"/enhance/{job_id}")

    def edit(self, audio_url: str, **fields: Any) -> Dict[str, Any]:
        """Submit an audio-edit job. Bills audio_seconds."""
        data = {"audio_url": audio_url, **{k: v for k, v in fields.items() if v is not None}}
        return self._request("POST", "/edit", data)

    def get_edit(self, job_id: str) -> Dict[str, Any]:
        """Retrieve edit result.

        Once the job is completed, the response is augmented with
        ``audio_url`` (R2 presigned URL, 7-day retention), ``expires_at``,
        and ``resemble_url`` (upstream fallback). See ``get_enhance`` for
        details — same mirror behavior.
        """
        return self._request("GET", f"/edit/{job_id}")
