
class ReportAPI:
    def __init__(self, client):
        self.client = client

    def get_tickets(self, restrict_by_locations=None):
        params = {}
        if restrict_by_locations:
            params["restrictByLocations"] = restrict_by_locations
        return self.client._post("api/report/tickets", params=params)

    def get_time_clocks(self, start_date, end_date, page_index=1, page_size=100, return_deleted=False, skip_time_zone_conversion=False):
        params = {
            "startDate": start_date,
            "endDate": end_date,
            "pageIndex": page_index,
            "pageSize": page_size,
            "returnDeleted": return_deleted,
            "skipTimeZoneConvertion": skip_time_zone_conversion
        }
        return self.client._get("api/report/timeClocks", params=params)
