"""Identity (beta): voice identity enrollment + search."""

from typing import Any, Dict

from ._base import _ResembleResource


class _Identity(_ResembleResource):
    _prefix = "/resemble/identity"

    def search(self, **fields: Any) -> Dict[str, Any]:
        """Search known identities by audio sample. Bills 1 search."""
        data = {k: v for k, v in fields.items() if v is not None}
        return self._request("POST", "/search", data)

    def enroll(self, **fields: Any) -> Dict[str, Any]:
        """Enroll a new identity. Bills 1 enrollment."""
        data = {k: v for k, v in fields.items() if v is not None}
        return self._request("POST", "/enroll", data)

    def list(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        return self._request("GET", f"?page={page}&page_size={page_size}")

    def get(self, identity_id: str) -> Dict[str, Any]:
        return self._request("GET", f"/{identity_id}")

    def delete(self, identity_id: str) -> Dict[str, Any]:
        return self._request("DELETE", f"/{identity_id}")
