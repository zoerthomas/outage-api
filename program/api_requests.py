import requests
from requests.adapters import HTTPAdapter, Retry
import os


BASE_URL = os.environ.get("BASE_URL")
SITE_ID = os.environ.get("SITE_ID")
API_KEY = os.environ.get("API_KEY")


session = requests.Session()
retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
session.mount('https://', HTTPAdapter(max_retries=retries))
session.headers.update({"x-api-key": API_KEY})

def get_request(url):
    try:
        response = session.get(url)
        response.raise_for_status()
        print(f"GET to {url} | StatusCode:{response.status_code}")
        return response.json()
    except requests.exceptions.HTTPError as HTTPError:
        status_code = HTTPError.response.status_code
        body = HTTPError.response.json()
        return {"statusCode": status_code, "message": body.get("message")}


def post_request(url, data):
    try:
        response = session.post(url, json=data)
        response.raise_for_status()
        print(f"POST to {url} | StatusCode:{response.status_code}")
        return response.json()
    except requests.exceptions.HTTPError as HTTPError:
        status_code = HTTPError.response.status_code  
        body = HTTPError.response.json()
        return {"statusCode": status_code, "message": body.get("message")}


def get_site_device_name_and_ids(site_id):
    url = f"https://{BASE_URL}/site-info/{site_id}"
    site_info = get_request(url)
    return site_info


def get_outages():
    url = f"https://{BASE_URL}/outages"
    outages = get_request(url)
    return outages


def post_outage_report(outage_report, site_id):
    outage_report = outage_report
    url = f"https://{BASE_URL}/site-outages/{site_id}"
    response = post_request(url, outage_report)
    return response
