"""Shared base for Resemble sub-resources."""

from typing import Any, Dict, Optional


class _ResembleResource:
    """Base for every Resemble sub-resource.

    Holds a reference to the parent Client and a path prefix, and exposes a
    thin _request() wrapper so sub-classes can call self._request("POST",
    "/tts/synthesize", data) without each one knowing the full path shape.
    """

    # Override in subclasses — e.g. "/resemble/tts".
    _prefix: str = "/resemble"

    def __init__(self, client) -> None:
        self._client = client

    def _path(self, suffix: str = "") -> str:
        if suffix and not suffix.startswith(("/", "?")):
            suffix = "/" + suffix
        return f"{self._prefix}{suffix}"

    def _request(
        self,
        method: str,
        suffix: str = "",
        data: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Any:
        endpoint = self._path(suffix).lstrip("/")
        return self._client._request(method, endpoint, data, **kwargs)
