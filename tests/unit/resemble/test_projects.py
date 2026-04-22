"""Unit tests for client.resemble.projects.* and .clips.*"""

import pytest


@pytest.mark.unit
def test_list_projects(mock_client):
    mock_client.resemble.projects.list(page=2, page_size=25)
    args = mock_client._request.call_args[0]
    assert args[0] == "GET"
    assert args[1] == "resemble/projects?page=2&page_size=25"


@pytest.mark.unit
def test_create_project(mock_client):
    mock_client.resemble.projects.create(name="MyProj", description="d")
    args = mock_client._request.call_args[0]
    assert args[0] == "POST"
    assert args[1] == "resemble/projects"
    assert args[2] == {"name": "MyProj", "description": "d"}


@pytest.mark.unit
def test_get_project(mock_client):
    mock_client.resemble.projects.get("p-1")
    assert mock_client._request.call_args[0][:2] == ("GET", "resemble/projects/p-1")


@pytest.mark.unit
def test_update_project(mock_client):
    mock_client.resemble.projects.update("p-1", name="renamed")
    args = mock_client._request.call_args[0]
    assert args[0] == "PUT"
    assert args[1] == "resemble/projects/p-1"
    assert args[2] == {"name": "renamed"}


@pytest.mark.unit
def test_delete_project(mock_client):
    mock_client.resemble.projects.delete("p-1")
    assert mock_client._request.call_args[0][:2] == ("DELETE", "resemble/projects/p-1")


@pytest.mark.unit
def test_list_clips(mock_client):
    mock_client.resemble.projects.clips.list("p-1")
    args = mock_client._request.call_args[0]
    assert args[0] == "GET"
    assert args[1] == "resemble/projects/p-1/clips?page=1&page_size=10"


@pytest.mark.unit
def test_create_clip(mock_client):
    mock_client.resemble.projects.clips.create("p-1", {"voice_uuid": "v-1", "text": "Hi"})
    args = mock_client._request.call_args[0]
    assert args[0] == "POST"
    assert args[1] == "resemble/projects/p-1/clips"
    assert args[2] == {"fields": {"voice_uuid": "v-1", "text": "Hi"}}


@pytest.mark.unit
def test_get_clip(mock_client):
    mock_client.resemble.projects.clips.get("p-1", "c-1")
    assert mock_client._request.call_args[0][:2] == ("GET", "resemble/projects/p-1/clips/c-1")


@pytest.mark.unit
def test_delete_clip(mock_client):
    mock_client.resemble.projects.clips.delete("p-1", "c-1")
    assert mock_client._request.call_args[0][:2] == ("DELETE", "resemble/projects/p-1/clips/c-1")
