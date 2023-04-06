def check_for_error(response):
    for item in response:
        if item == "statusCode":
            return True

def outage_report(outages, devices, exclude_before):
    outage_report = []
    outages_dict = outages
    devices_dict = devices
    if check_for_error(outages_dict):
        return(f"Issue retrieving outage info. Received the following error: {outages_dict}")
    elif check_for_error(devices_dict):
        return(f"Issue retrieving device info. Received the following error: {devices_dict}")
    else:
        for outage in outages_dict:
            if outage["begin"] >= exclude_before:
                for device in devices_dict["devices"]:
                    if outage["id"] == device["id"]:
                        outage["name"] = device["name"]
                        outage_report.append(outage)
        return outage_report

