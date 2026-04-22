"""Projects + nested Clips. Pure metadata, free CRUD."""

from typing import Any, Dict

from ._base import _ResembleResource


class _Clips(_ResembleResource):
    """Nested under /resemble/projects/{project_uuid}/clips."""

    _prefix = "/resemble/projects"

    def _cpath(self, project_uuid: str, suffix: str = "") -> str:
        base = f"/{project_uuid}/clips"
        if suffix and not suffix.startswith(("/", "?")):
            suffix = "/" + suffix
        return base + suffix

    def list(self, project_uuid: str, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        return self._request(
            "GET",
            self._cpath(project_uuid, f"?page={page}&page_size={page_size}"),
        )

    def create(self, project_uuid: str, fields: Dict[str, Any]) -> Dict[str, Any]:
        return self._request("POST", self._cpath(project_uuid), {"fields": fields})

    def get(self, project_uuid: str, clip_uuid: str) -> Dict[str, Any]:
        return self._request("GET", self._cpath(project_uuid, clip_uuid))

    def delete(self, project_uuid: str, clip_uuid: str) -> Dict[str, Any]:
        return self._request("DELETE", self._cpath(project_uuid, clip_uuid))


class _Projects(_ResembleResource):
    _prefix = "/resemble/projects"

    def __init__(self, client) -> None:
        super().__init__(client)
        self.clips = _Clips(client)

    def list(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        return self._request("GET", f"?page={page}&page_size={page_size}")

    def create(self, name: str, **fields: Any) -> Dict[str, Any]:
        data = {"name": name, **{k: v for k, v in fields.items() if v is not None}}
        return self._request("POST", "", data)

    def get(self, project_uuid: str) -> Dict[str, Any]:
        return self._request("GET", f"/{project_uuid}")

    def update(self, project_uuid: str, **fields: Any) -> Dict[str, Any]:
        data = {k: v for k, v in fields.items() if v is not None}
        return self._request("PUT", f"/{project_uuid}", data)

    def delete(self, project_uuid: str) -> Dict[str, Any]:
        return self._request("DELETE", f"/{project_uuid}")
