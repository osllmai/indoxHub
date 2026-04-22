"""Safety: deepfake detection, content intelligence, audio source tracing.

All three follow the same async submit/retrieve pattern. Paths are siblings
under /resemble (detect, intelligence, tracing) so we do not use a single
prefix.
"""

from typing import Any, Dict

from ._base import _ResembleResource


class _Safety(_ResembleResource):
    _prefix = "/resemble"

    def _submit(self, capability: str, fields: Dict[str, Any]) -> Dict[str, Any]:
        data = {k: v for k, v in fields.items() if v is not None}
        return self._request("POST", f"/{capability}", data)

    def _get(self, capability: str, job_id: str) -> Dict[str, Any]:
        return self._request("GET", f"/{capability}/{job_id}")

    # --- Deepfake detection (audio / video / image) ---

    def detect(self, **fields: Any) -> Dict[str, Any]:
        """Submit a deepfake-detection job. Bills by modality."""
        return self._submit("detect", fields)

    def get_detect(self, job_id: str) -> Dict[str, Any]:
        return self._get("detect", job_id)

    # --- Content intelligence ---

    def intelligence(self, **fields: Any) -> Dict[str, Any]:
        """Submit a content-intelligence job (audio/video/image)."""
        return self._submit("intelligence", fields)

    def get_intelligence(self, job_id: str) -> Dict[str, Any]:
        return self._get("intelligence", job_id)

    # --- Audio source tracing ---

    def tracing(self, **fields: Any) -> Dict[str, Any]:
        """Submit an audio-source-tracing job."""
        return self._submit("tracing", fields)

    def get_tracing(self, job_id: str) -> Dict[str, Any]:
        return self._get("tracing", job_id)
