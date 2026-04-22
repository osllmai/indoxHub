"""Text-to-Speech: synchronous synth + voice listing."""

from typing import Any, Dict, Optional

from ._base import _ResembleResource


class _TTS(_ResembleResource):
    _prefix = "/resemble/tts"

    def synthesize(
        self,
        voice_uuid: str,
        text: str,
        output_format: str = "mp3",
        precision: Optional[str] = None,
        sample_rate: Optional[int] = None,
        language: Optional[str] = None,
        speed: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Synchronous text-to-speech. Bills audio_seconds.

        Returns the server payload verbatim, including:
          - audio_content (base64)
          - audio_duration (float, seconds)
          - billing {unit, quantity, charged}
          - request_id
          - raw_response (original Resemble body)
        """
        data: Dict[str, Any] = {
            "voice_uuid": voice_uuid,
            "text": text,
            "output_format": output_format,
        }
        if precision is not None:
            data["precision"] = precision
        if sample_rate is not None:
            data["sample_rate"] = sample_rate
        if language is not None:
            data["language"] = language
        if speed is not None:
            data["speed"] = speed
        return self._request("POST", "/synthesize", data)

    def list_voices(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """List the account's voices. Free. page_size must be 10–1000."""
        return self._request(
            "GET",
            f"/voices?page={page}&page_size={page_size}",
        )

    def get_voice(self, voice_uuid: str) -> Dict[str, Any]:
        """Get one voice's metadata. Free."""
        return self._request("GET", f"/voices/{voice_uuid}")
