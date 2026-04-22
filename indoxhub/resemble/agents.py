"""Agents + Tools + Webhooks + Knowledge Base.

Resemble's agent platform exposes four sibling resources, all sharing the
same CRUD shape. We build a tiny CRUD mixin and apply it to four classes
with different prefixes.
"""

from typing import Any, Dict

from ._base import _ResembleResource


class _CRUD(_ResembleResource):
    """Generic list/create/get/update/delete over an arbitrary prefix.

    Subclasses set _prefix to the resource path. The server expects a
    `{"fields": {...}}` envelope on POST/PUT bodies — we wrap automatically.
    """

    def list(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        return self._request("GET", f"?page={page}&page_size={page_size}")

    def create(self, fields: Dict[str, Any]) -> Dict[str, Any]:
        return self._request("POST", "", {"fields": fields})

    def get(self, uuid: str) -> Dict[str, Any]:
        return self._request("GET", f"/{uuid}")

    def update(self, uuid: str, fields: Dict[str, Any]) -> Dict[str, Any]:
        return self._request("PUT", f"/{uuid}", {"fields": fields})

    def delete(self, uuid: str) -> Dict[str, Any]:
        return self._request("DELETE", f"/{uuid}")


class _Agents(_CRUD):
    _prefix = "/resemble/agents"

    def capabilities(self) -> Dict[str, Any]:
        return self._request("GET", "/capabilities")

    def system_tools(self) -> Dict[str, Any]:
        return self._request("GET", "/system-tools")


class _AgentTools(_CRUD):
    _prefix = "/resemble/agent-tools"


class _AgentWebhooks(_CRUD):
    _prefix = "/resemble/agent-webhooks"


class _KnowledgeBase(_CRUD):
    _prefix = "/resemble/knowledge-base"
