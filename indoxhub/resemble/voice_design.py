"""Voice Design. Requires Resemble Business plan (server gates with 503)."""

from typing import Any, Dict, Optional

from ._base import _ResembleResource


class _VoiceDesign(_ResembleResource):
    _prefix = "/resemble/voice-design"

    def generate_candidates(
        self,
        description: str,
        sample_text: Optional[str] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Generate candidate voices from a text description.

        Raises ResembleBusinessPlanError if the deployment's Business plan
        gate is off.
        """
        data: Dict[str, Any] = {"description": description}
        if sample_text is not None:
            data["sample_text"] = sample_text
        if params is not None:
            data["params"] = params
        return self._request("POST", "/candidates", data)

    def promote(
        self,
        design_uuid: str,
        candidate_index: int,
        name: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Promote one candidate into a real voice. Business-plan only."""
        data: Dict[str, Any] = {
            "candidate_index": candidate_index,
            "name": name,
        }
        if params is not None:
            data["params"] = params
        return self._request("POST", f"/{design_uuid}/promote", data)
