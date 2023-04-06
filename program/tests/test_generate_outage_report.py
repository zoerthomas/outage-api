import json

from ..generate_outage_report import outage_report
from .test_data import mock_post_outage_data, mock_get_outage_response, mock_get_site_info_response

OUTAGES = json.loads(mock_get_outage_response.outage_response)
DEVICES = json.loads(mock_get_site_info_response.site_info)
EXCLUDE_BEFORE = "2022-01-01T00:00:00.000Z"

def test_generate_outage_report():
    expected_outage_report = json.loads(mock_post_outage_data.outage_data)
    result = outage_report(OUTAGES, DEVICES, EXCLUDE_BEFORE)
    assert expected_outage_report == result

def test_error_response_from_outages():
    mock_400_error_response = {"statusCode":"400",
                          "message": "We cannot process your request because it doesn't match the required format."}
    result = outage_report(mock_400_error_response, DEVICES, EXCLUDE_BEFORE)
    assert result == f"Issue retrieving outage info. Received the following error: {mock_400_error_response}"


def test_error_response_from_devices():
    mock_400_error_response = {"statusCode":"400",
                          "message": "We cannot process your request because it doesn't match the required format."}
    result = outage_report(OUTAGES, mock_400_error_response, EXCLUDE_BEFORE)
    assert result == f"Issue retrieving device info. Received the following error: {mock_400_error_response}"
