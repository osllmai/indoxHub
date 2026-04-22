"""Voice cloning. Requires Resemble Business plan (server gates with 503)."""

from typing import Any, Dict, Optional

from ._base import _ResembleResource


class _Voices(_ResembleResource):
    _prefix = "/resemble/voices"

    def create(
        self,
        name: str,
        consent_text: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Create a new voice (cloning). Business-plan only.

        Raises ResembleBusinessPlanError if RESEMBLE_BUSINESS_PLAN_ACTIVE is
        false on the connected deployment.
        """
        data: Dict[str, Any] = {"name": name}
        if consent_text is not None:
            data["consent_text"] = consent_text
        if description is not None:
            data["description"] = description
        return self._request("POST", "", data)

    def build(
        self,
        voice_uuid: str,
        recording_ids: Optional[list] = None,
    ) -> Dict[str, Any]:
        """Build (train) a voice from its enrolled recordings.
        Writes a voice_subscriptions usage record. Business-plan only.
        """
        data: Dict[str, Any] = {}
        if recording_ids is not None:
            data["recording_ids"] = recording_ids
        return self._request("POST", f"/{voice_uuid}/build", data)

    def delete(self, voice_uuid: str) -> Dict[str, Any]:
        """Delete a voice. Free. Not Business-plan gated."""
        return self._request("DELETE", f"/{voice_uuid}")
