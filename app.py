import os
from program import api_requests
from program.generate_outage_report import outage_report
from dotenv import load_dotenv

load_dotenv()


def get_and_post_outage_data_for_specific_site(site_id):
    device_info = api_requests.get_site_device_name_and_ids(site_id)
    outages = api_requests.get_outages()
    exclude_before = os.environ.get("EXCLUDE_BEFORE")
    report = outage_report(outages, device_info, exclude_before)
    result = api_requests.post_outage_report(report, site_id)
    return result


get_and_post_outage_data_for_specific_site(os.environ.get("SITE_ID"))
