"""Uploads: multipart pass-through to IndoxHub storage (Cloudflare R2)."""

from typing import Any, Dict, Optional

from ._base import _ResembleResource


class _Uploads(_ResembleResource):
    _prefix = "/resemble/uploads"

    def create(self, file_path: str, purpose: Optional[str] = None) -> Dict[str, Any]:
        """Upload a local file and receive back a presigned R2 URL.

        Args:
            file_path: path to a local audio/video/image file.
            purpose: optional retention hint. One of:
                - ``voice_clone`` -> voice-recordings/ prefix, **PERMANENT** retention.
                  Use for voice-clone source recordings (identity asset).
                - ``stt_input`` -> stt-input/ prefix, 30-day retention.
                - ``watermark_input`` -> watermark/ prefix, 7-day retention.
                - ``audio_job_input`` -> audio-jobs/ prefix, 7-day retention.
                - ``None`` (default) -> uploads/ prefix, 30-day retention.

        Returns the server payload, which includes:
            - ``url``: presigned R2 URL valid for 1 hour. Pass this as
              ``audio_url`` / ``video_url`` into STT, enhance, edit, detect,
              intelligence, watermark, or identity endpoints.
            - ``expires_at`` (ISO 8601 string or None): when the file will
              be auto-deleted. ``None`` means permanent (e.g. voice clones).
            - ``asset_class``, ``asset_id``, ``size_bytes``, ``file_name``,
              ``extension``, ``file_type``.

        Example:
            >>> client.resemble.uploads.create("voice.wav", purpose="voice_clone")
            {'url': 'https://...', 'expires_at': None, 'asset_class': 'voice_recordings', ...}
        """
        with open(file_path, "rb") as f:
            files = {"file": f}
            data = {"purpose": purpose} if purpose else None
            return self._request("POST", "", data=data, files=files)
