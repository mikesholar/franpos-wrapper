
import requests
from .endpoints import (
    classes, reports, company, datadump, purchase_order,
    employee, common, walkin, customer, import_module, booking, pos
)

class FranPOSClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://publicapi.franpos.com/"
        self.headers = {"Content-Type": "application/json"}
        self.params = {"Token": self.api_key}

        self.classes = classes.ClassAPI(self)
        self.reports = reports.ReportAPI(self)
        self.company = company.CompanyAPI(self)
        self.datadump = datadump.DataDumpAPI(self)
        self.purchase_order = purchase_order.PurchaseOrderAPI(self)
        self.employee = employee.EmployeeAPI(self)
        self.common = common.CommonAPI(self)
        self.walkin = walkin.WalkInAPI(self)
        self.customer = customer.CustomerAPI(self)
        self.import_module = import_module.ImportAPI(self)
        self.booking = booking.BookingAPI(self)
        self.pos = pos.PosAPI(self)

    def _get(self, path, params=None):
        all_params = self.params.copy()
        if params:
            all_params.update(params)
        response = requests.get(f"{self.base_url}{path}", headers=self.headers, params=all_params)
        response.raise_for_status()
        return response.json()

    def _post(self, path, json=None, params=None):
        all_params = self.params.copy()
        if params:
            all_params.update(params)
        response = requests.post(f"{self.base_url}{path}", headers=self.headers, params=all_params, json=json)
        response.raise_for_status()
        return response.json()
