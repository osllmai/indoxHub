"""Unit tests for client.resemble.agents.* + tools/webhooks/knowledge_base."""

import pytest


@pytest.mark.unit
@pytest.mark.parametrize(
    "namespace,prefix",
    [
        ("agents", "resemble/agents"),
        ("agent_tools", "resemble/agent-tools"),
        ("agent_webhooks", "resemble/agent-webhooks"),
        ("knowledge_base", "resemble/knowledge-base"),
    ],
)
class TestSharedCRUD:
    """Same CRUD surface across all four agent sub-resources."""

    def test_list(self, mock_client, namespace, prefix):
        getattr(mock_client.resemble, namespace).list(page=1, page_size=10)
        args = mock_client._request.call_args[0]
        assert args[0] == "GET"
        assert args[1] == f"{prefix}?page=1&page_size=10"

    def test_create(self, mock_client, namespace, prefix):
        getattr(mock_client.resemble, namespace).create({"name": "x"})
        args = mock_client._request.call_args[0]
        assert args[0] == "POST"
        assert args[1] == prefix
        assert args[2] == {"fields": {"name": "x"}}

    def test_get(self, mock_client, namespace, prefix):
        getattr(mock_client.resemble, namespace).get("u-1")
        assert mock_client._request.call_args[0][:2] == ("GET", f"{prefix}/u-1")

    def test_update(self, mock_client, namespace, prefix):
        getattr(mock_client.resemble, namespace).update("u-1", {"name": "y"})
        args = mock_client._request.call_args[0]
        assert args[0] == "PUT"
        assert args[1] == f"{prefix}/u-1"
        assert args[2] == {"fields": {"name": "y"}}

    def test_delete(self, mock_client, namespace, prefix):
        getattr(mock_client.resemble, namespace).delete("u-1")
        assert mock_client._request.call_args[0][:2] == ("DELETE", f"{prefix}/u-1")


@pytest.mark.unit
def test_agents_capabilities(mock_client):
    mock_client.resemble.agents.capabilities()
    assert mock_client._request.call_args[0][:2] == ("GET", "resemble/agents/capabilities")


@pytest.mark.unit
def test_agents_system_tools(mock_client):
    mock_client.resemble.agents.system_tools()
    assert mock_client._request.call_args[0][:2] == ("GET", "resemble/agents/system-tools")
