"""Recordings (training audio nested under a voice). Free CRUD."""

from typing import Any, Dict

from ._base import _ResembleResource


class _Recordings(_ResembleResource):
    """Prefix is dynamic — set per-call since it's nested under voice_uuid."""

    _prefix = "/resemble/voices"

    def _rec_path(self, voice_uuid: str, suffix: str = "") -> str:
        base = f"/{voice_uuid}/recordings"
        if suffix and not suffix.startswith("/"):
            suffix = "/" + suffix
        return base + suffix

    def list(
        self,
        voice_uuid: str,
        page: int = 1,
        page_size: int = 10,
    ) -> Dict[str, Any]:
        return self._request(
            "GET",
            f"{self._rec_path(voice_uuid)}?page={page}&page_size={page_size}",
        )

    def create(self, voice_uuid: str, fields: Dict[str, Any]) -> Dict[str, Any]:
        return self._request(
            "POST",
            self._rec_path(voice_uuid),
            {"fields": fields},
        )

    def get(self, voice_uuid: str, recording_uuid: str) -> Dict[str, Any]:
        return self._request("GET", self._rec_path(voice_uuid, recording_uuid))

    def update(
        self, voice_uuid: str, recording_uuid: str, fields: Dict[str, Any]
    ) -> Dict[str, Any]:
        return self._request(
            "PUT",
            self._rec_path(voice_uuid, recording_uuid),
            {"fields": fields},
        )

    def delete(self, voice_uuid: str, recording_uuid: str) -> Dict[str, Any]:
        return self._request("DELETE", self._rec_path(voice_uuid, recording_uuid))
