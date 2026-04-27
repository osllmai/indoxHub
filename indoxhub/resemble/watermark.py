"""Watermark: apply + detect audio provenance markers."""

from typing import Any, Dict

from ._base import _ResembleResource


class _Watermark(_ResembleResource):
    _prefix = "/resemble/watermark"

    def apply(self, audio_url: str, **fields: Any) -> Dict[str, Any]:
        """Embed an inaudible watermark. Bills $0.0005/sec."""
        data = {"audio_url": audio_url, **{k: v for k, v in fields.items() if v is not None}}
        return self._request("POST", "/apply", data)

    def get_apply(self, job_id: str) -> Dict[str, Any]:
        """Retrieve watermark-apply result.

        Once the job is completed, the response is augmented with
        ``audio_url`` (R2 presigned URL, 7-day retention), ``expires_at``,
        and ``resemble_url`` (upstream fallback). Mirroring is lazy +
        idempotent.
        """
        return self._request("GET", f"/apply/{job_id}")

    def detect(self, audio_url: str, **fields: Any) -> Dict[str, Any]:
        """Detect watermark presence. Bills $0.0002/sec."""
        data = {"audio_url": audio_url, **{k: v for k, v in fields.items() if v is not None}}
        return self._request("POST", "/detect", data)

    def get_detect(self, job_id: str) -> Dict[str, Any]:
        return self._request("GET", f"/detect/{job_id}")
