"""Verify the server's 503 Business-plan gate maps to ResembleBusinessPlanError."""

from unittest.mock import MagicMock, patch

import pytest
import requests

from indoxhub import Client, ResembleBusinessPlanError


@pytest.mark.unit
def test_503_business_plan_maps_to_specific_exception():
    with patch.object(Client, "_authenticate", return_value=None):
        client = Client(api_key="test")

        # Fake an HTTP 503 with the server's Business-plan gate phrase
        mock_response = MagicMock()
        mock_response.status_code = 503
        mock_response.json.return_value = {
            "detail": "This capability requires a Resemble Business-plan subscription, which is not active on this deployment."
        }
        http_error = requests.HTTPError(response=mock_response)
        mock_response.raise_for_status.side_effect = http_error

        with patch.object(client.session, "request", return_value=mock_response):
            with pytest.raises(ResembleBusinessPlanError) as excinfo:
                client._request("POST", "resemble/voices", {"name": "x"})
            assert "Business-plan" in str(excinfo.value)
        client.close()
